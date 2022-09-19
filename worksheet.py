import xlsxwriter
import random


def worksheet_writer(carrier_list):
    row, col = 0, 0
    new_workbook = xlsxwriter.Workbook("sheet.xlsx")
    new_sheet = new_workbook.add_worksheet()
    for i in (random.sample(carrier_list, 30)):
        new_sheet.write(row, col, i["mbl"])
        col += 1
        new_sheet.write(row, col, i["container"])
        col += 1
        new_sheet.write(row, col, i["carrier"])
        row += 1
        col = 0
    new_workbook.close()
    print("Done")
