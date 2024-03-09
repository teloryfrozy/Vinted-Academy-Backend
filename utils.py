"""File that handles mechanisms of the discount module.

verify the conformity of input data in the module
Pre processing of data before applying the main algorithm
"""


def get_data_file(file_path) -> list:
    """Returns the list of rows in file."""
    with open(file_path) as f:
        rows = f.readlines()

    return rows


def display_data(data):
    """Prints data to the console as STDOUT."""
    for out in data:
        output = []
        for item in out:
            if not isinstance(item, str):
                item = "%.2f" % item
            output.append(item)
        print(" ".join(output))


def get_lowest_price(provider_pricing: dict[dict], package_size="S") -> float:
    """Returns smallest price from price list according to package size.
    :param provider_pricing:
    :param package_size:
    :return: string:
    """
    prices = []
    for key, value in provider_pricing.items():
        for size, price in value.items():
            if size == package_size:
                prices.append(price)
    prices.sort()

    return prices[:1][0]


def verify_input_file_format(file_name: str, allowed_formats: list) -> bool:
    """Checks if the input file format is valid."""
    file_extension = file_name.split(".")[1]

    if file_extension not in allowed_formats:
        print(f"Invalid file format. Only {allowed_formats} files are expected.")
        exit(1)

    return True


def verify_date_format(date: str, allowed_format: str, current_date: list[int]) -> bool:
    """Verify if date is in right format."""
    INVALID_DATE = "Invalid date format. "

    try:
        date_divided = date.split("-")

        if len(date_divided) != 3:
            print(f"{INVALID_DATE}Only {allowed_format} is allowed.")
            exit(1)
        year, month, day = date_divided

        if len(year) != 4:
            print(f"{INVALID_DATE}Year must contains 4 digits.")
            exit(1)
        elif len(month) != 2:
            print(f"{INVALID_DATE}Month must contains 2 digits.")
            exit(1)
        elif len(day) != 2:
            print(f"{INVALID_DATE}Day must contains 2 digits.")
            exit(1)

        year, month, day = map(int, date_divided)

        # This test may be added if it fits the requirements
        current_year, current_month, current_day = current_date
        if year > current_year or (
            year == current_year
            and (
                month > current_month or (month == current_month and day > current_day)
            )
        ):
            print(f"{INVALID_DATE}Input date is greater than current date")
            exit(1)

        if year < 2013:
            print(
                f"{INVALID_DATE}Year must be greater than or equal to 2013 (Vinted launched in France)."
            )
            exit(1)
        elif year > 2024:
            print(f"{INVALID_DATE}Year must be lower than or equal to 2024.")
            exit(1)
        elif month < 1:
            print(f"{INVALID_DATE}Month must be greater than or equal to 1.")
            exit(1)
        elif month > 12:
            print(f"{INVALID_DATE}Month must be lower than or equal to 12.")
            exit(1)
        elif day < 1:
            print(f"{INVALID_DATE}Day must be greater than or equal to 1.")
            exit(1)
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
                        exit(1)

    except ValueError:
        print(
            f"{INVALID_DATE}Only integers are allowed using this format: {allowed_format}."
        )
        exit(1)

    return True
