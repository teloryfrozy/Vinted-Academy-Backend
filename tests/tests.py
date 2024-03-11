"""Data Tests Module.

Defines tests to assert the good functioning of the module.
"""

import unittest

DATA = {
    "LP": {"S": "1.50", "M": "4.90", "L": "6.90"},
    "MR": {"S": "2.00", "M": "3.00", "L": "4.00"},
}

ALLOWED_SIZES = ["S", "M", "L"]
LOWEST_PRICE = "1.50"
TEST_FILE = "test.txt"
PROVIDERS_COUNT = len(DATA)



# TEST most of functions success and fail 1 class = 1 file


"""
TestShipmentHelper(unittest.TestCase)
    
    test if len(input) = len(all rows after sorting)

    todo change names
    def test_get_providers(self):
        providers = ShipmentHelper.get_providers(DATA)
        self.assertEqual(len(providers), PROVIDERS_COUNT)


        def test_get_lowest_price(self):
        price = ShipmentHelper.get_lowest_price(DATA)
        self.assertEqual(LOWEST_PRICE, price)
        self.assertNotEqual(LOWEST_PRICE, "0.00")

    def test_get_price(self):
        price = ShipmentHelper.get_price("LP", "L", DATA)
        self.assertEqual("6.90", price)
        self.assertNotEqual("4.90", price)
        

        test_get_price_package (test with hard coded value)

        
        

        
         def test_get_all_package_sizes(self):
        sizes = ShipmentHelper.get_package_sizes(DATA)
        all_sizes = True
        for size in sizes:
            if size not in ALLOWED_SIZES:
                all_sizes = False
        self.assertEqual(len(sizes), 3)
        self.assertTrue(all_sizes)
    """

   


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
