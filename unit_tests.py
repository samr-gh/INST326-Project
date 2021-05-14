""" Documentation: 

    Our project scrapes data off of the FootLocker website in order to use that data to 
    help shoppers find particular shoes.  We do this by scraping data off of the main site,
    then scraping individual shoe data and saving those attributes that we have scraped.
    Once we have saved the individual shoe attributes, we are then able to use those attributes
    in a function that would simplify the shopping experience for the user online.
    
    In order to run our program, the user would need to input certain criteria of a shoe and then run the program.
    
    To interpret the output of the program, you would see the shoe that best fits the user criteria and satisfies what they
    are searching for."""
    
#These are planned unit tests
import unittest
from automated import Data
from site import store_features

class TestAuto(unittest.TestCase):
    def test_productfl(self):
        url = "https://www.footlocker.com/category/womens/shoes.html?currentPage=0"
        s = Data.scrape(url)
        result = Data.get_product_fl(s)
        self.assertEqual(result, dict)
    
    def test_productlink(self):
        url = "https://www.footlocker.com/category/womens/shoes.html?currentPage=0"
        b = Data.get_product_link(url)
        self.assertEqual(b, [])
        
    def test_scrape(self):
        url = "https://www.footlocker.com/category/womens/shoes.html?currentPage=0"
        j = Data.scrape(url)
        self.assertEqual(j, [])
  
  
  
  
		# assertRaisesRegex(int(prices), 'prices')
        # assertRaisesRegex(product_num,'product_num')
		# (float(ValueError, 'Not a number')) 
			
		#This is to test scape uses only mens or only womens shoes links
		# assertEqual d.scrape(shoe_links,'mens')
			
		#This is to test that we get the required list of links 
		# assertListEqual Data.get_product_link == [] 
class TestSite(unittest.TestCase):
    def test_storefeatures(self):
        self.assertEqual(store_features.csv, dict)
    
