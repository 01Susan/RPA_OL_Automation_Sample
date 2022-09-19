import pandas as pd
from validator import check_key, is_nan, total_csv_line
from worksheet import worksheet_writer
import sys


def main(filename):
    carrier_list = []
    csv = pd.read_csv(filename, usecols=["Container #", "MBL Number", "Carrier Name"])
    column = csv.columns
    carrier, mbl, container = list(csv["Carrier Name"].values), list(csv["MBL Number"].values), list(
        csv["Container #"].values)
    csv_length = total_csv_line(filename)

    for i in range(csv_length - 1):
        if not is_nan(carrier[i]) and not is_nan(mbl[i]) and not is_nan(container[i]):
            if check_key(carrier[i], carrier_list):
                carrier_list.append({
                    "carrier": carrier[i],
                    "mbl": mbl[i],
                    "container": container[i]
                })

    worksheet_writer(carrier_list)


filename_user = ""
try:
    filename_user = sys.argv[1].replace('"', "")
except IndexError:
    filename_user = input("Enter the File Path: \n").replace('"', "")

main(filename_user)
