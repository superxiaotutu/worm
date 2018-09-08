import os

import xlrd
import xlutils.copy
import xlwt
import xlsxwriter

from python_worm.common_function import clear_char
xls_file=""
wb = xlrd.open_workbook(xls_file)
sheet = wb.sheet_by_index(0)
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
    with open(A+"/"+B+"/"+C+"/"+D+"0001.jpg") as f :
        print(D)