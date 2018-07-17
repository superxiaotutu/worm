import re
import json
import random
import re
import os
import socket
import string
import threading
import time
import urllib.request
import urllib.error
import requests
import xlrd
from bs4 import BeautifulSoup
import pymongo
from common_function import clear_char

TAG_URL_OF_WEAPON = 'url_of_weapon'
TAG_URL_OF_CACHE = 'url_of_cache'
BASE_URL = 'http://weapon.huanqiu.com'
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["huanqiu"]


# db.create_collection('key_url')


# col = db["key_url"]
def request_url(url):
    data = requests.get(url)
    # col = db["cache_url"]
    # source = col.find_one({'url': url})
    # if source:
    #     return source['source']
    # else:
    #     print(url)
    #     col.insert_one({
    #         'tag': TAG_URL_OF_CACHE,
    #         'url': url,
    #         'source': data.text
    #     })
    return data.text


# def insert_urlofweapon():
#     col = db["key_url"]
#     col.insert_one({
#         'tag': TAG_URL_OF_WEAPON,
#         'url': url
#         'name': name
#     })


def get_weapon_url(source, keyname):
    # col = db["key_url"]
    soup = BeautifulSoup(source, 'html.parser')
    li = soup.find('li', class_="img")
    url = li.find('a').get('href')
    url = BASE_URL + url
    # if col.find_one({'name': keyname}):
    #     col.replace_one(
    #         {'name': keyname},
    #         {
    #             'tag': TAG_URL_OF_WEAPON,
    #             'url': url,
    #             'name': keyname
    #         })
    # else:
    #     col.insert_one({
    #         'tag': TAG_URL_OF_WEAPON,
    #         'url': url,
    #         'name': keyname
    #     })


def get_weapon_info(keyname,source):
    # data_info=''
    #
    # col = db["key_url"]
    # result = col.find_one({'name': keyname})
    # if col.find_one({'name': keyname}):

    soup = BeautifulSoup(source, 'html.parser')
    li = soup.find('li', class_="img")
    url = li.find('a').get('href')
    url = BASE_URL + url

    # url = result['url']
    source = request_url(url)
    soup = BeautifulSoup(source, 'html.parser')
    data_info = soup.find('div', class_='dataInfo')
    data_info = data_info.text
    try:
        intron = soup.find('div', class_='intron')
        intron = intron.text
        info = soup.find('div', class_='info')
        info = info.text
    except Exception as e:
        info = ''
        intron = ''
        print(e)
    with open('dirlist', 'r', encoding='utf8') as f_r:
        dirs_lines = f_r.readlines()
        for l in dirs_lines:
            if keyname in l:
                dirname = '../' + l.strip('\n')
                with open(dirname + '/info.txt', 'a',encoding='utf8') as f:
                    f.write(data_info)
                    f.write(info)
                    f.write(intron)
                try:
                    img = soup.find('div', class_="maxPic")
                    img = img.find('img').get('src')
                    res = requests.get(img)
                    res.raw.decode_content = True
                    print(img)

                    if res.status_code == 200:
                        # str(random.randint(0, 9999))
                        with open(dirname + os.sep + '0001' + '.jpg', 'wb') as image_f:
                            image_f.write(res.content)
                except Exception as e:
                    print(e)


if __name__ == '__main__':
    xls_file = '../../cfg/list.xlsx'
    wb = xlrd.open_workbook(xls_file)
    sheet = wb.sheet_by_index(0)
    for irow in range(3367,sheet.nrows):
        print(irow)
        c_row = sheet.row(irow)
        # A = c_row[0].value
        # B = c_row[1].value
        # C = c_row[2].value
        D = c_row[3].value
        # A = clear_char(A)
        # B = clear_char(B)
        # C = clear_char(C)
        D = clear_char(D)
        print(D)
        # keyname = 'C-295中程预警机'
        keyname = D
        search_url = 'http://weapon.huanqiu.com/search?keyword='
        url = 'http://weapon.huanqiu.com/search?keyword=' + keyname
        keyname = clear_char(keyname)

        # data=request_url(url)
        # query = {"tag":TAG_URL_OF_WEAPON}
        # col.delete_many(query)
        try:
            source = request_url(url)
            # print(source)
            # get_weapon_url(source, keyname)
            get_weapon_info(keyname,source)
            # print(request_url('http://weapon.huanqiu.com/c_295'))
        except:
            continue
