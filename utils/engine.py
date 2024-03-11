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
        invalid_dates = {}
        valid_rows = []

        # Retrieving valid dates
        for row in self.rows:
            date = row.split()[0]
            if not DataValidator.verify_date_format(date):
                index_date = self.rows.index(row)
                invalid_dates[date] = (index_date, row)
            else:
                valid_rows.append(row)

        valid_rows.sort(
            key=lambda row: datetime.datetime.strptime(row.split()[0], "%Y-%m-%d")
        )

        # Setting data back in ascending order
        result = []
        for valid_row in valid_rows:
            result.append(valid_row)

        if len(invalid_dates) > 0:
            for index_date, invalid_row in invalid_dates.values():
                result.insert(index_date, invalid_row)

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
                if self.discount_left < 1.0:
                        print(round(self.discount_left, 2), "DIFF", difference)
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

        # print(self.discount_left, row.split())

        # if row.split()[0] == "2023-02-18":
        #     print("test")
        #     shipment_price = round(float(shipment_price), 2)
        #     if discount != STRAW:
        #         discount = round(float(discount), 2)
        #     print(self.discount_left, shipment_price, discount)
        #     print("test")

        # As we are working with float we must round them
        shipment_price = round(float(shipment_price), 2)
        if discount != STRAW:
            discount = round(float(discount), 2)

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

                row = self.apply_discount(row.strip())
                self.rows[i] = row

    @staticmethod
    def display_data(rows: list[str]):
        """Prints shipment rows as STDOUT."""
        for row in rows:
            print(row, end="")
