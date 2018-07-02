import os

import pymongo
import xlrd
import xlutils.copy
import xlwt
import xlsxwriter

from python_worm.common_function import clear_char

xls_file='../cfg/list.xlsx'
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["runoobdb"]
wb = xlrd.open_workbook(xls_file)
sheet = wb.sheet_by_index(0)
for irow in range(sheet.nrows):
    c_row = sheet.row(irow)
    A = c_row[0].value
    B = c_row[1].value
    C = c_row[2].value
    D = c_row[3].value
    A=clear_char(A)
    B=clear_char(B)
    C=clear_char(C)
    D=clear_char(D)
    dir=A
    if not os.path.isdir('../Data/环球军事网/'+dir):
        os.mkdir('../Data/环球军事网/'+dir)
    dir = A + '/' + B
    if not os.path.isdir('../Data/环球军事网/' + dir):
        os.mkdir('../Data/环球军事网/' + dir)
    dir = A + '/' + B
    if not os.path.isdir('../Data/环球军事网/' + dir):
        os.mkdir('../Data/环球军事网/' + dir)
    dir = A + '/' + B + '/' + C
    if not os.path.isdir('../Data/环球军事网/' + dir):
        os.mkdir('../Data/环球军事网/' + dir)
    dir = A + '/' + B + '/' + C +'/' + D
    if not os.path.isdir('../Data/环球军事网/' + dir):
        os.mkdir('../Data/环球军事网/' + dir)
    print(A,B,C,D)
