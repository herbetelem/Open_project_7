import xlrd
import numpy as np

workbook = xlrd.open_workbook('action_to_buy.xlsx')
SheetNameList = workbook.sheet_names()
for i in np.arange( len(SheetNameList) ):
    print( SheetNameList[i] )