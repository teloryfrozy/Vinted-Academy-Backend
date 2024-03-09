class DataAccessor:

    @staticmethod
    def get_lowest_price(provider_prices: dict[dict[float]], package_size) -> float:
        """Returns smallest price among package size prices."""
        prices = []

        for shipper in provider_prices.values():
            for size, price in shipper.items():
                if size == package_size:
                    prices.append(price)

        return float(min(prices))

    @staticmethod
    def get_data_file(file_path: str) -> list:
        """Returns the list of rows in file."""
        with open(file_path) as f:
            rows = f.readlines()

        return rows

    @staticmethod
    def get_price_package(provider: str, size: str, shipper_prices: dict) -> float:
        """Returns price according to selected provider and package size."""
        return float(shipper_prices[provider][size])

    @staticmethod
    def get_all_sizes(shipper_prices: dict) -> list:
        """Returns all available package sizes"""
        sizes = []
        for shipper in shipper_prices.values():
            for size in shipper.keys():
                if size not in sizes:
                    sizes.append(size)
        return sizes

    @staticmethod
    def get_all_shippers(shipper_prices: dict) -> list:
        """Returns all available shipper companies."""
        return shipper_prices.keys()
