import unittest
from ..stock import Stock
class StockTest(unittest.TestCase):
    def test_price_of_new_class_should_be_None(self):
        stock = Stock("GOOG")
        self.assertIsNone(stock.price)

# When this file is run from the command line name contains main. This is not executed when this class is imported
if __name__ == "__main__":
    unittest.main()

