import os
import shutil

from python_worm.common_function import clear_char
import re

file_list = []
path_list=[]

def walk_static_dir(dirPath):
    if not os.path.isdir(dirPath):
        return
    files = os.listdir(dirPath)
    try:
        for file in files:
            filePath = os.path.join(dirPath, file)
            if os.path.isfile(filePath):
                filePath_temp=filePath
                clear_char(filePath)
                res = re.search('\\\\(.+)', filePath[len('../Data/huanqiu\\'):-4]).group(1)
                file_list.append(res)

                path_list.append(filePath_temp)
            elif os.path.isdir(filePath):
                walk_static_dir(filePath)
                pass
    except Exception as e:
        raise e


def walk_static_dir1(dirPath):
    if not os.path.isdir(dirPath):
        return
    files = os.listdir(dirPath)
    try:
        for file in files:
            filePath = os.path.join(dirPath, file)
            if os.path.isfile(filePath):
                pass
                # print(filePath)
                # os.remove(filePath)
            elif os.path.isdir(filePath):
                if clear_char(file) in file_list:
                    inde=(file_list.index(clear_char(file)))
                    print(path_list[inde]+filePath)
                    shutil.copy(path_list[inde],filePath+'/0001.jpg')
                walk_static_dir1(filePath)

    except Exception as e:
        raise e

walk_static_dir('../Data/huanqiu')
walk_static_dir1('../Data/环球军事网')
# st='高射炮\JP113式37毫米双管高射炮'
# res = re.search('\\\\(.+)', st).group(1)
# print(res)
