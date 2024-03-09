"""Handles all algorithms with the data."""

import datetime
from data_accessor import DataAccessor
from data_validator import DataValidator
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
)


class DataProcessing(DataAccessor):

    def __init__(self, shipper_prices: dict[dict[float]], file_path: str, current_date: list[int]):
        self.shipper_prices = shipper_prices
        self.rows = DataAccessor.get_data_file(file_path)
        self.data_validator = DataValidator(shipper_prices, file_path)
        self.current_date = current_date
        self.invalid_line,            
        self.discount_max_amount,
        self.no_discount,
        self.small_package,
        self.large_package,
        self.free_shipment,
        self.free_provider,

    def sort_asc_by_date(self):
        """Sorts rows by date in ascending order."""
        # Retrieving dates
        dates = []
        for item in self.rows:
            dates.append(item.split()[0])

        # Retrieving invalid dates
        invalid_dates = {}
        for date in dates:
            if not DataValidator.verify_date_format(
                date, self.current_date
            ):
                index_date = dates.index(date)
                dates.remove(date)
                invalid_dates[index_date] = date

        dates_asc_list = sorted(
            dates, key=lambda x: datetime.datetime.strptime(x, "%Y-%m-%d")
        )

        if len(invalid_dates.keys()) > 0:
            for index_date, date in invalid_dates.items():
                dates_asc_list.insert(index_date, date)

        # Setting data back in ascending order
        result = []
        for date in dates_asc_list:
            for key in self.rows:
                if date in key.split():
                    result.append(key)
                    break
        self.rows = result

    def get_discount(self, package_size: str, shipper: str, discount_max_amount: int) -> tuple[str, str]:
        """Returns the shipment price and the discount if there is one."""
        ...
        shipment_price = DataAccessor.get_price_package(shipper, package_size, self.shipper_prices)
        "2015-02-01 S MR"
        if 

    def apply_discount(self, row: list, invalid_line: str, discount_max_amount: int) -> list:
        """Appplies a discount to the row if the requirements are matched."""
        if self.data_validator.verify_row(row, self.current_date) is False:
            row.append(invalid_line)
        else:
            package_size, shipper = row.split()[1:]
            discount = self.get_discount(package_size, shipper, discount_max_amount)
            row.append(discount)

        return row

    def process_transactions(
        self,
        invalid_line,            
        discount_max_amount,
        no_discount,
        small_package,
        large_package,
        free_shipment,
        free_provider,
    ):
        """Process all rows and add discounts according to the requirements."""
        self.discount_left = 0
        year = ...
        month = ...
        day = ...
        # TODO RESET THE discount_left each first row from a new month

    @staticmethod
    def display_data(rows: list):
        """Prints shipment rows as STDOUT."""
        for row in rows:
            print(row, end="")
