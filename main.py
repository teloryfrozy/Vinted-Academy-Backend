"""Shipment Discount Main Module.

Handles the execution of the shipment discount algorithm, processing input data and displaying results.
"""

__version__ = "1.0.0"
__author__ = "Augustin ROLET"
__license__ = "MIT"
__description__ = "Main module for handling shipment discount algorithms."


import sys
from utils.constants import DEFAULT_PATH
from utils.data_validator import DataValidator
from utils.engine import DataProcessor

if sys.version_info < (3, 11, 2):
    print(
        "[WARNING] This module has been developed with Python 3.11.2. Using an older version may lead to issues."
    )


def main() -> int:
    """Main function that executes the shipment discount algorithm"""
    data_processor = DataProcessor(input_path)
    data_processor.sort_asc_by_date()
    data_processor.process_transactions()
    data_processor.display_data(data_processor.rows)
    exit(0)


try:
    if len(sys.argv) > 2:
        print("Invalid command. More than 2 arguments provided.")
        exit(1)

    input_path = sys.argv[1]
    file_name = input_path.split("/")[-1]

    DataValidator.verify_input_file_format(file_name)
except IndexError:
    input_path = DEFAULT_PATH


if __name__ == "__main__":
    main()
