"""Data Validator module.

Ensures data integrity validity of input data
"""

from utils.data_accessor import DataAccessor
from utils.constants import (
    ALLOWED_FILE_FORMATS,
    CURRENT_DATE_SPLITED,
    SHIPPERS_PRICES,
    STRAW,
)


class DataValidator(DataAccessor):

    def __init__(self, file_path: str):
        self.rows = DataAccessor.get_data_file(file_path)
        self.all_sizes = DataAccessor.get_all_sizes()
        self.all_shippers = DataAccessor.get_all_shippers()

    def verify_row(self, row: str) -> bool:
        """Verify the format of the row."""
        splitted_data = row.split()

        if len(splitted_data) != 3:
            return False
        if DataValidator.verify_date_format(splitted_data[0]) is False:
            return False
        if splitted_data[1] not in DataAccessor.get_all_sizes():
            return False
        if splitted_data[2] not in DataAccessor.get_all_shippers():
            return False
        if SHIPPERS_PRICES.get(splitted_data[2], {}).get(splitted_data[1]) is None:
            return False
        return True

    def verify_shipper(self, shipper: str) -> bool:
        """Verify if provider exist."""
        return shipper in self.all_shippers

    def verify_package_size(self, size: str):
        """Verify if size exist."""
        return size in self.all_sizes

    @staticmethod
    def verify_input_file_format(file_name: str) -> bool:
        """Verify if the input file format is valid."""
        file_extension = file_name.split(".")[1]

        if file_extension not in ALLOWED_FILE_FORMATS:
            print(
                f"Invalid file format. Only {ALLOWED_FILE_FORMATS} files are expected."
            )
            exit(1)

        return True

    @staticmethod
    def verify_date_format(date: str) -> bool:
        """Verify if date is in right format."""
        try:
            # I chose not to print the reason for date invalidity,
            # but I retained the various cases I handled, detailed.
            date_divided = date.split(STRAW)

            if len(date_divided) != 3:
                return False

            year, month, day = date_divided

            if len(year) != 4:
                return False
            elif len(month) != 2:
                return False
            elif len(day) != 2:
                return False

            year, month, day = map(int, date_divided)

            current_year, current_month, current_day = CURRENT_DATE_SPLITED
            if year > current_year or (
                year == current_year
                and (
                    month > current_month
                    or (month == current_month and day > current_day)
                )
            ):
                return False

            if year < 2013:  # Vinted's French launch year
                return False
            elif year > 2024:
                return False
            elif month < 1:
                return False
            elif month > 12:
                return False
            elif day < 1:
                return False
            else:
                for i in range(1, 13):
                    if month == i:
                        if month == 2:
                            is_leap_year = (year % 4 == 0 and year % 100 != 0) or (
                                year % 400 == 0
                            )
                            last_day = 29 if is_leap_year else 28
                        else:
                            last_day = 30 if i % 2 == 0 and i != 8 else 31

                        if day > last_day:
                            return False

        except ValueError:
            return False

        return True
