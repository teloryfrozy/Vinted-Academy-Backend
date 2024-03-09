"""Constants for the discount calculation module are defined here"""

import datetime
from data_accessor import DataAccessor


def get_current_date_splited():
    current_date_time = datetime.datetime.now()
    current_date = current_date_time.date()
    return list(map(str.upper, map(int, str(current_date).split("-"))))


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
FREE_PROVIDER = "LP"
CURRENT_DATE_SPLITED = get_current_date_splited()
ALL_SHIPPERS = DataAccessor.get_all_shippers()
ALL_SIZES = DataAccessor.get_all_sizes()
