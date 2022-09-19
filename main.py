import math
import random
import xlsxwriter
import pandas as pd

csv = pd.read_csv("OL.csv", usecols=["Container #", "MBL Number", "Carrier Name"])
column = csv.columns
carrier = list(csv["Carrier Name"].values)
mbl = list(csv["MBL Number"].values)
container = list(csv["Container #"].values)
new_list = []
row, col = 0, 0
sum_var = 0
with open("OL.csv", encoding="cp850") as f:
    sum_var = sum(1 for line in f)


def is_nan(x):
    try:
        return math.isnan(x)
    except:
        return False


def checkKey(carrier_name, carrier_list):
    for i in carrier_list:
        if i["carrier"] == carrier_name:
            return False
    return True


for i in range(1, sum_var - 1):
    try:
        if not is_nan(carrier[i]) and not is_nan(mbl[i]) and not is_nan(container[i]):
            if checkKey(carrier[i], new_list):
                new_list.append({
                    "carrier": carrier[i],
                    "mbl": mbl[i],
                    "container": container[i]
                })
    except:
        pass

new_workbook = xlsxwriter.Workbook("sheet.xlsx")
new_sheet = new_workbook.add_worksheet()
for i in (random.sample(new_list, 30)):
    new_sheet.write(row, col, i["mbl"])
    col += 1
    new_sheet.write(row, col, i["container"])
    col += 1
    new_sheet.write(row, col, i["carrier"])
    row += 1
    col = 0
new_workbook.close()
