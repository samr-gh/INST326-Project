"""We could not figure out how to test the functions in automated.py as 
    they are very complex and specific. 
    
    We also did not write tests for some functions in site.py as most do not 
    return anything. 
"""

import unittest
from automated import Data
from site import parse_args

class TestFunctions(unittest.TestCase):
    def test_get_product_fl(self):
        url = "https://www.footlocker.com/product/ugg-oh-yeah-slide-womens/7953BLK.html"
        name = Data.get_product_fl(url).get("Name")
        gender = Data.get_product_fl(url).get("Gender")
        colors = Data.get_product_fl(url).get("Colors")
        price = Data.get_product_fl(url).get("Price")
        sizes = Data.get_product_fl(url).get("Sizes")
        prod_ID = Data.get_product_fl(url).get("Product ID")
        self.assertEqual({"Name": name,
            "Gender": gender,
            "Colors": colors, "Price": price, 
            "Sizes": sizes,
            "Product ID": prod_ID}, {"Name": 
            "UGG Oh Yeah Slide", "Gender": "Women's",
            "Colors": "Black/Black", "Price": 100.0, 
            "Sizes": "05.006.007.008.009.010.011.012.0",
            "Product ID": "7953BLKSay"})

    def test_parse_args(self):
        args_list = ["--gender M", "--attributes black", "--PATH test.path"]
        self.assertEqual(parse_args(args_list), ["M", "black", "test.path"])
        
if __name__ == "__main__":
    unittest.main()
    
