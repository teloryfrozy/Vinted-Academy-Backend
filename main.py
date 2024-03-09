"""Main file that handles the engine and run functions

All constant for the modules are defined here
"""

__version__ = "0.1"
__author__ = "Augustin ROLET"


import datetime
import sys

if sys.version_info < (3, 11, 2):
    print(
        "[WARNING] This module has been developed with Python 3.11.2. Using an older version may lead to issues."
    )

SHIPPERS_PRICES = {
    "LP": {"S": "1.50", "M": "4.90", "L": "6.90"},
    "MR": {"S": "2.00", "M": "3.00", "L": "4.00"},
}
DISCOUNT_MAX_AMOUNT = 10
DEFAULT_PATH = "input.txt"
ALLOWED_FILE_FORMATS = ["txt"]
DATE_FORMAT = "YYYY-MM-DD"
INVALID_LINE = "Ignored"
FREE_SHIPMENT = "0.00"
NO_DISCOUNT = "-"
LARGE_PACKAGE = "L"
SMALL_PACKAGE = "S"
FREE_PROVIDER = "LP"


try:
    if len(sys.argv) > 2:
        print("Invalid command. More than 2 arguments provided.")
        exit(1)

    INPUT_PATH = sys.argv[1]
except IndexError:
    INPUT_PATH = DEFAULT_PATH


current_date_time = datetime.datetime.now()
current_date = current_date_time.date()
current_date_splited = map(int, str(current_date).split("-"))
print(current_date_splited)

exit(0)
