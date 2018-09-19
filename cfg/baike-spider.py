from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq
import os
import time
import re


browser = webdriver.Chrome()
wait = WebDriverWait(browser, 3)

def search(name):
    try:
        browser.get('https://baike.baidu.com/search')
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#query'))
        )
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#search'))
        )
        input.send_keys(name)
        submit.click()
        browser.refresh()
        clickinto(name)
        #GetInfo()
    except TimeoutException:
        print('error')

def clickinto(name):
    try:
        click = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#body_wrapper > div.searchResult > dl > dd:nth-child(2) > a'))
        )
        click.click()
        GetInfo1(name)
    except TimeoutException:
        GetInfo(name)


def GetInfo(name):
    try:
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.body-wrapper > div.content-wrapper > div > div.main-content > div.lemma-summary'))
        )
        time.sleep(1)
        info = browser.find_element_by_class_name("lemma-summary").text
        print(info)
        filename = name + '.txt'
        f_write = open(filename,'ab+')
        f_write.write((info+'\r\n').encode('UTF-8'))
        f_write.close()
    except TimeoutException:
        print('error')

def GetInfo1(name):
    try:
        handles = browser.window_handles
        browser.switch_to.window(handles[-1])
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.body-wrapper > div.content-wrapper > div > div.main-content > div.lemma-summary'))
        )
        time.sleep(1)
        info = browser.find_element_by_class_name("lemma-summary").text
        print(info)
        filename = name + '.txt'
        f_write = open(filename, 'ab+')
        f_write.write((info + '\r\n' + '\n').encode('UTF-8'))
        f_write.close()
        browser.close()
        handles = browser.window_handles
        browser.switch_to.window(handles[-1])
    except TimeoutException:
        print('error')
        handles = browser.window_handles
        browser.switch_to.window(handles[0])
        browser.close()
        browser.switch_to.window(handles[-1])

def GetNameList():
    f = open("1.txt")
    all_lines = f.readlines()
    data = []
    for line in all_lines:
        temp = line.strip('\n')
        temp = re.sub('[/]','',temp)
        temp = temp.replace(' ','')
        temp = temp.replace('?','')
        data.append(temp)
    for i in data:
        search(i)
    f.close()

def main():
    #search('F/RF-101E“魔术师”')
    GetNameList()

if __name__ == '__main__':
    main()
