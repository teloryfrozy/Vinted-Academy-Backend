"""Data Accessor Module.

Provides methods for retrieving data to the algorithm from predefined constants.
"""

from utils.constants import BREAK_LINE, SHIPPERS_PRICES


class DataAccessor:

    @staticmethod
    def get_lowest_price(package_size: str) -> float:
        """Returns smallest price among package size prices."""
        prices = []

        for shipper in SHIPPERS_PRICES.values():
            for size, price in shipper.items():
                if size == package_size:
                    prices.append(price)

        return float(min(prices))

    @staticmethod
    def get_data_file(file_path: str) -> list[str]:
        """Returns the list of rows in file."""
        with open(file_path) as f:
            rows = f.readlines()

        rows[-1] += BREAK_LINE

        return rows

    @staticmethod
    def get_price_package(shipper: str, size: str) -> float:
        """Returns price according to selected shipper and package size."""
        return float(SHIPPERS_PRICES[shipper][size])

    @staticmethod
    def get_all_sizes() -> list:
        """Returns all available package sizes"""
        sizes = set()
        for shipper in SHIPPERS_PRICES.values():
            for size in shipper.keys():
                if size not in sizes:
                    sizes.add(size)

        return list(sizes)

    @staticmethod
    def get_all_shippers():
        """Returns all available shipper companies."""
        return SHIPPERS_PRICES.keys()
