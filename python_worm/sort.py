import os

import xlrd
import xlutils.copy
import xlwt
import xlsxwriter

from python_worm.common_function import clear_char

xls_file = "../cfg/list.xlsx"
wb = xlrd.open_workbook(xls_file)
sheet = wb.sheet_by_index(0)
temp_C = ""
index = 0
for irow in range(sheet.nrows):
    c_row = sheet.row(irow)
    A = c_row[0].value
    B = c_row[1].value
    C = c_row[2].value
    D = c_row[3].value
    A = clear_char(A)
    B = clear_char(B)
    C = clear_char(C)
    D = clear_char(D)
    if os.path.isfile("../Data/环球军事网/" + A + "/" + B + "/" + C + "/" + D + "/0001.jpg"):
        if not temp_C:
            temp_C = C
        if C == temp_C:
            print(C)
            print(index)

            if C == "":
                pa = "环球军事网/" + A + "/" + B + "/" + D + "/0001.jpg"
                with open("name.txt", 'a',encoding='utf8') as f:
                    f.write(pa + " " + str(index) + " " + B +"\n")
            else:
                pa = "环球军事网/" + A + "/" + B + "/" + C + "/" + D + "/0001.jpg"
                with open("name.txt", 'a',encoding='utf8') as f:
                    f.write(pa + " " + str(index) + " " + C +"\n")
        else:
            index += 1
        temp_C = C
