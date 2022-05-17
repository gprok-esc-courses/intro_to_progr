import xlrd


excel = xlrd.open_workbook("data/weatherdata.xls")
sheet = excel.sheet_by_index(1)

for row in sheet:
    print(row)