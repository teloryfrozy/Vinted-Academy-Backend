"""Main file that handles the engine and run functions"""

__version__ = "0.1"
__author__ = "Augustin ROLET"


import datetime
import sys
from data_validator import DataValidator

if sys.version_info < (3, 11, 2):
    print(
        "[WARNING] This module has been developed with Python 3.11.2. Using an older version may lead to issues."
    )

SHIPPERS_PRICES = {
    "LP": {"S": 1.50, "M": 4.90, "L": 6.90},
    "MR": {"S": 2.00, "M": 3.00, "L": 4.00},
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


def main() -> int:
    """Main function that executes the shipment discount algorithm"""
    if DataValidator.verify_input_file_format(FILE_NAME, ALLOWED_FILE_FORMATS):
        print("test")

    current_date_time = datetime.datetime.now()
    current_date = current_date_time.date()
    current_date_splited = str(current_date).split("-")
    current_date_splited = list(map(int, current_date_splited))
    print(current_date_splited)

    exit(0)


try:
    if len(sys.argv) > 2:
        print("Invalid command. More than 2 arguments provided.")
        exit(1)

    input_path = sys.argv[1]
    FILE_NAME = input_path.split("/")[-1]
except IndexError:
    FILE_NAME = DEFAULT_PATH


main()
