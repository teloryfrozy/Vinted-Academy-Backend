"""Main file that handles the engine and run functions"""

__version__ = "0.1"
__author__ = "Augustin ROLET"


import sys
from data_validator import DataValidator
from engine import DataProcessing
from constants import (
    SHIPPERS_PRICES,
    DISCOUNT_MAX_AMOUNT,
    DEFAULT_PATH,
    ALLOWED_FILE_FORMATS,
    INVALID_LINE,
    FREE_SHIPMENT,
    FREE_PROVIDER,
    NO_DISCOUNT,
    LARGE_PACKAGE,
    SMALL_PACKAGE,
    CURRENT_DATE_SPLITED,
)

if sys.version_info < (3, 11, 2):
    print(
        "[WARNING] This module has been developed with Python 3.11.2. Using an older version may lead to issues."
    )


def main() -> int:
    """Main function that executes the shipment discount algorithm"""

    data_processing = DataProcessing(SHIPPERS_PRICES, input_path, CURRENT_DATE_SPLITED)
    data_processing.sort_asc_by_date()
    data_processing.display_data(data_processing.rows)
    data_processing.process_transactions(
        INVALID_LINE,
        DISCOUNT_MAX_AMOUNT,
        NO_DISCOUNT,
        SMALL_PACKAGE,
        LARGE_PACKAGE,
        FREE_SHIPMENT,
        FREE_PROVIDER,
    )
    exit(0)


try:
    if len(sys.argv) > 2:
        print("Invalid command. More than 2 arguments provided.")
        exit(1)

    input_path = sys.argv[1]
    file_name = input_path.split("/")[-1]

    DataValidator.verify_input_file_format(file_name, ALLOWED_FILE_FORMATS)
except IndexError:
    input_path = DEFAULT_PATH


main()
