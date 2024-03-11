"""Data Tests Module.

Defines tests to assert the good functioning of the module.
"""

import unittest
import sys
import os

project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.abspath(os.path.join(project_root, "..")))

from utils.constants import SMALL_PACKAGE
from utils.data_accessor import DataAccessor
from utils.data_validator import DataValidator


class TestDataAccessor(unittest.TestCase):

    def test_get_lowest_price(self):
        lowest_price = DataAccessor.get_lowest_price(SMALL_PACKAGE)
        self.assertEqual(lowest_price, 1.50)

    def test_get_price_package(self):
        price = DataAccessor.get_price_package("LP", "M")
        self.assertEqual(price, 4.90)

    def test_get_all_sizes(self):
        result = sorted(DataAccessor.get_all_sizes())
        sizes = sorted(["M", "L", "S"])
        self.assertEqual(result, sizes)

    def test_get_all_shippers(self):
        result = sorted(DataAccessor.get_all_shippers())
        shippers = sorted(["MR", "LP"])
        self.assertEqual(result, shippers)


class TestDataValidator(unittest.TestCase):

    def setUp(self):
        self.data_validator = DataValidator("tests/test.txt")

    def test_verify_row_success(self):
        rows = [
            "2015-02-05 S LP",
            "2015-02-13 M LP",
            "2015-02-09 L LP",
            "2015-02-06 S MR",
            "2015-02-08 M MR",
            "2015-02-07 L MR",
        ]
        for row in rows:
            self.assertTrue(self.data_validator.verify_row(row))

    def test_verify_row_failure(self):
        rows = ["02-05-2015 S LP", "2015-02-29 CUSPS", "I love Vinted"]
        for row in rows:
            self.assertFalse(self.data_validator.verify_row(row))

    def test_verify_shipper_success(self):
        shippers = ["MR", "LP"]
        for shipper in shippers:
            self.assertTrue(self.data_validator.verify_shipper(shipper))

    def test_verify_shipper_failure(self):
        shippers = ["UPS", "RC"]
        for shipper in shippers:
            self.assertFalse(self.data_validator.verify_shipper(shipper))

    def test_verify_package_size_success(self):
        sizes = ["S", "M", "L"]
        for size in sizes:
            self.assertTrue(self.data_validator.verify_package_size(size))

    def test_verify_package_size_failure(self):
        sizes = ["XS", "XL", "XXL"]
        for size in sizes:
            self.assertFalse(self.data_validator.verify_package_size(size))

    def test_verify_input_file_format_success(self):
        result = DataValidator.verify_input_file_format("test.txt")

        self.assertTrue(result)

    def test_verify_input_file_format_failure(self):
        with self.assertRaises(SystemExit):
            DataValidator.verify_input_file_format("test.json")

    def test_verify_date_format_success(self):
        self.assertTrue(DataValidator.verify_date_format("2015-02-08"))

    def test_verify_date_format_failure(self):
        dates = [
            "02-08-2015",
            "08-02-2015",
            "08/02/2015",
            "8/02/2015",
            "8/02/15",
            "8/2/15",
            "02-08-2025",
            "29-02-2023",
            "-1-08-2015",
            "02-13-2015",
        ]
        for date in dates:
            self.assertFalse(DataValidator.verify_date_format(date))


class TestDataProcessor(unittest.TestCase):
    

    def setUp(self) -> None:
        return super().setUp()
    
    def test_sort_asc_by_date(self):
        ...

        # original = ShipmentHelper.read_file(TEST_FILE)
        # data = ShipmentProcessor.order_data_asc(ShipmentHelper.read_file(TEST_FILE))
        # self.assertEqual(len(original), len(data))



"""class TestShipmentProcessor(unittest.TestCase):


def test_process_data(self):
        content = ShipmentProcessor.order_data_asc(ShipmentHelper.read_file(TEST_FILE))
        data = ShipmentProcessor.process_data(
            content, DATA, "S", "L", "Ignore", "LP", "0.00", 10
        )
        len before sorting = len after sorting
        self.assertEqual(len(content), len(data))


    def test_order_data_asc(self):
        original = ShipmentHelper.read_file(TEST_FILE)
        data = ShipmentProcessor.order_data_asc(ShipmentHelper.read_file(TEST_FILE))
        self.assertEqual(len(original), len(data))
        self.assertNotEqual(original, data)

    def test_output_data(self):
        output = ShipmentProcessor.output_data(ShipmentHelper.read_file(TEST_FILE))
        ordered_output = ShipmentProcessor.order_data_asc(
            ShipmentHelper.read_file(TEST_FILE)
        )
        self.assertTrue(output)
        self.assertTrue(ordered_output)"""


if __name__ == "__main__":
    unittest.main()
