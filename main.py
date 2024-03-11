"""Main file that handles the engine and run functions"""

__version__ = "0.1"
__author__ = "Augustin ROLET"


import sys
from utils.constants import ALLOWED_FILE_FORMATS, DEFAULT_PATH
from utils.data_validator import DataValidator
from utils.engine import DataProcessing

if sys.version_info < (3, 11, 2):
    print(
        "[WARNING] This module has been developed with Python 3.11.2. Using an older version may lead to issues."
    )


def main() -> int:
    """Main function that executes the shipment discount algorithm"""
    data_processing = DataProcessing(input_path)
    data_processing.sort_asc_by_date()
    data_processing.process_transactions()
    data_processing.display_data(data_processing.rows)
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
