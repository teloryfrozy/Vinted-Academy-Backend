"""Data Processor Module.

Handles data algorithms necessary for the main shipment discount module.
"""

import datetime
from utils.data_accessor import DataAccessor
from utils.data_validator import DataValidator
from utils.constants import (
    BREAK_LINE,
    FREE_SHIPMENT,
    INVALID_LINE,
    LARGE_PACKAGE,
    STRAW,
    FREE_SHIPPER,
    OUT_OF_DISCOUNT,
    SMALL_PACKAGE,
    DISCOUNT_MAX_AMOUNT,
)


class DataProcessor(DataAccessor):

    def __init__(self, file_path: str):
        self.rows = DataAccessor.get_data_file(file_path)
        self.data_validator = DataValidator(file_path)

    def sort_asc_by_date(self):
        """Sorts rows by date in ascending order."""
        # Retrieving dates
        dates = []
        for row in self.rows:
            dates.append(row.split()[0])

        # Retrieving invalid dates
        invalid_dates = {}
        for date in dates:
            if not DataValidator.verify_date_format(date):
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

    def get_discount(self, package_size: str, shipper: str) -> tuple[str, str]:
        """Returns the shipment price and the discount if there is one."""
        shipment_price = DataAccessor.get_price_package(shipper, package_size)

        if self.discount_left == OUT_OF_DISCOUNT:
            return (shipment_price, STRAW)

        if package_size != SMALL_PACKAGE and shipper != FREE_SHIPPER:
            return (shipment_price, STRAW)

        if shipper == FREE_SHIPPER:
            if package_size != LARGE_PACKAGE:
                return (shipment_price, STRAW)
            else:
                if self.large_month_count == 2:
                    if self.discount_left >= shipment_price:
                        self.discount_left -= shipment_price
                        self.large_month_count += 1
                        return (FREE_SHIPMENT, shipment_price)
                    else:
                        discount = self.discount_left
                        shipment_price_left = shipment_price - self.discount_left
                        self.discount_left = OUT_OF_DISCOUNT
                        self.large_month_count += 1
                        return (shipment_price_left, discount)
                else:
                    self.large_month_count += 1
                    return (shipment_price, STRAW)

        if package_size == SMALL_PACKAGE:
            lowest_price = DataAccessor.get_lowest_price(package_size)
            if shipment_price == lowest_price:
                return (shipment_price, STRAW)
            else:
                difference = shipment_price - lowest_price
                if difference <= self.discount_left:
                    self.discount_left -= difference
                    return (lowest_price, difference)
                else:
                    difference -= self.discount_left
                    self.discount_left = OUT_OF_DISCOUNT
                    return (shipment_price - difference, difference)

    def apply_discount(self, row: str) -> str:
        """Appplies a discount to the row if the requirements are matched."""
        package_size, shipper = row.split()[1:]
        shipment_price, discount = self.get_discount(package_size, shipper)
        row += f" {shipment_price} {discount}{BREAK_LINE}"

        return row

    def process_transactions(self):
        """Process all rows and add discounts according to the requirements."""
        current_month = None

        for i, row in enumerate(self.rows):
            row = row.rstrip(BREAK_LINE)

            if self.data_validator.verify_row(row) is False:
                row += f" {INVALID_LINE}{BREAK_LINE}"
                self.rows[i] = row
            else:
                row_list = row.split()
                date = row_list[0].split(STRAW)
                month = date[1]

                if current_month != month:
                    self.discount_left = DISCOUNT_MAX_AMOUNT
                    self.large_month_count = 0
                    current_month = month

                row = self.apply_discount(row)
                self.rows[i] = row

    @staticmethod
    def display_data(rows: list[str]):
        """Prints shipment rows as STDOUT."""
        for row in rows:
            print(row, end="")
