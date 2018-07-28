import os
import shutil

from python_worm.common_function import clear_char
import re

file_list = []
path_list=[]
ori_pathlist=[]
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
                try:
                    result = re.search("\\\\(.+)", dirPath).group(1)
                    result = re.search("\\\\(.+)", result).group(1)
                    result = re.search("\\\\(.+)", result).group(1)
                    result = re.search("\\\\(.+)", result).group(1)
                except:
                    result = re.search("\\\\(.+)", dirPath).group(1)
                    result = re.search("\\\\(.+)", result).group(1)
                    result = re.search("\\\\(.+)", result).group(1)
                    # print(clear_char(result))
                finally:
                    path_list.append(clear_char(result))
                    ori_pathlist.append(dirPath)
                # file_list.append(res)
                # path_list.append(filePath_temp)
                # print(filePath_temp)
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
                # print(dirPath)
                # print(filePath)
                # os.remove(filePath)
            elif os.path.isdir(filePath):
                print(filePath)
                if clear_char(file) in file_list:
                    pass
                    # inde=(file_list.index(clear_char(file)))
                    # print(path_list[inde]+filePath)
                    # shutil.copy(path_list[inde],filePath+'/0001.jpg')
                walk_static_dir1(filePath)

    except Exception as e:
        raise e

walk_static_dir('../Data/环球军事网')
# walk_static_dir1('../Data/环球军事网')
# st='高射炮\JP113式37毫米双管高射炮'
# res = re.search('\\\\(.+)', st).group(1)
# print(res)
# for r,d,f in os.walk('../cfg/'):
#     for i in f:
#         if i[:-4] in path_list:
#             print(i[:-4])
#             print(ori_pathlist[path_list.index(i[:-4])])
#             path=ori_pathlist[path_list.index(i[:-4])]
#             shutil.move('../cfg/'+i,path)



