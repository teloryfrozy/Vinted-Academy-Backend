"""Constants for the discount calculation module are defined here"""

import datetime


def get_current_date_splited():
    current_date_time = datetime.datetime.now()
    current_date = current_date_time.date()
    return list(map(int, str(current_date).split("-")))


SHIPPERS_PRICES = {
    "LP": {"S": 1.50, "M": 4.90, "L": 6.90},
    "MR": {"S": 2.00, "M": 3.00, "L": 4.00},
}
DISCOUNT_MAX_AMOUNT = 10
DEFAULT_PATH = "input.txt"
ALLOWED_FILE_FORMATS = ["txt"]
INVALID_LINE = "Ignored"
FREE_SHIPMENT = "0.00"
NO_DISCOUNT = "-"
LARGE_PACKAGE = "L"
SMALL_PACKAGE = "S"
FREE_SHIPPER = "LP"
BREAK_LINE = '\n'
CURRENT_DATE_SPLITED = get_current_date_splited()
