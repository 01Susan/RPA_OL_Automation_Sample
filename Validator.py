import math


def check_key(carrier_name, carrier_list):
    for i in carrier_list:
        if i["carrier"] == carrier_name:
            return False
    return True


# Validator
def is_nan(x):
    try:
        return math.isnan(x)
    except TypeError:
        return False


def total_csv_line(filename):
    with open(filename, encoding="cp850") as f:
        sum_var = sum(1 for line in f)
        return sum_var

