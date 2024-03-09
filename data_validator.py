"""File that handles mechanisms of the discount module.

verify the conformity of input data in the module
Pre processing of data before applying the main algorithm
"""

from data_accessor import DataAccessor


class DataValidator(DataAccessor):

    def __init__(self, shipper_prices: dict[dict[float]], file_path: str):
        self.shipper_prices = shipper_prices
        self.rows = DataAccessor.get_data_file(file_path)
        self.all_sizes = DataAccessor.get_all_sizes(self.shipper_prices)
        self.all_shippers = DataAccessor.get_all_shippers(self.shipper_prices)

    def verify_row(
        self, row: str, date_allowed_format: str, current_date: list[int]
    ) -> bool:
        """Verify the format of the row."""
        splitted_data = row.split()

        if len(splitted_data) != 3:
            return False
        if (
            DataValidator.verify_date_format(
                splitted_data[0], date_allowed_format, current_date
            )
            is False
        ):
            return False
        if splitted_data[1] not in DataAccessor.get_all_sizes():
            return False
        if splitted_data[2] not in DataAccessor.get_all_shippers():
            return False
        if self.shipper_prices.get(splitted_data[2], {}).get(splitted_data[1]) is None:
            return False
        return True

    def verify_provider(self, shipper: str) -> bool:
        """Verify if provider is in data set."""
        return shipper in self.all_shippers

    def verify_package_size(self, size: str):
        """Verify if size is in data set."""
        return size in self.all_sizes

    @staticmethod
    def verify_input_file_format(file_name: str, allowed_formats: list) -> bool:
        """Verify if the input file format is valid."""
        file_extension = file_name.split(".")[1]

        if file_extension not in allowed_formats:
            print(f"Invalid file format. Only {allowed_formats} files are expected.")
            exit(1)

        return True

    @staticmethod
    def verify_date_format(
        date: str, allowed_format: str, current_date: list[int]
    ) -> bool:
        """Verify if date is in right format."""
        INVALID_DATE = "Invalid date format. "

        try:
            date_divided = date.split("-")

            if len(date_divided) != 3:
                print(f"{INVALID_DATE}Only {allowed_format} is allowed.")
                return False

            year, month, day = date_divided

            if len(year) != 4:
                print(f"{INVALID_DATE}Year must contains 4 digits.")
                return False
            elif len(month) != 2:
                print(f"{INVALID_DATE}Month must contains 2 digits.")
                return False
            elif len(day) != 2:
                print(f"{INVALID_DATE}Day must contains 2 digits.")
                return False

            year, month, day = map(int, date_divided)

            # This test may be added if it fits the requirements
            current_year, current_month, current_day = current_date
            if year > current_year or (
                year == current_year
                and (
                    month > current_month
                    or (month == current_month and day > current_day)
                )
            ):
                print(f"{INVALID_DATE}Input date is greater than current date")
                return False

            if year < 2013:
                print(
                    f"{INVALID_DATE}Year must be greater than or equal to 2013 (Vinted launched in France)."
                )
                return False
            elif year > 2024:
                print(f"{INVALID_DATE}Year must be lower than or equal to 2024.")
                return False
            elif month < 1:
                print(f"{INVALID_DATE}Month must be greater than or equal to 1.")
                return False
            elif month > 12:
                print(f"{INVALID_DATE}Month must be lower than or equal to 12.")
                return False
            elif day < 1:
                print(f"{INVALID_DATE}Day must be greater than or equal to 1.")
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
                            print(
                                f"{INVALID_DATE}Day must be lower than or equal to {last_day}."
                            )
                            return False

        except ValueError:
            print(
                f"{INVALID_DATE}Only integers are allowed using this format: {allowed_format}."
            )
            return False

        return True
