
"""This is code that was for a part of the project, but after talking with
Instructor Cruz we are taking a different approach and using Selenium. 
We are keeping this code here just in case as well to show the progress
that we had made before the change. 

Disregard this code. 
"""
import urllib.request
from bs4 import BeautifulSoup
import time

def get_product_fl(site):
     """Takes a Footlocker web page as a parameter and returns the product
          details as a string. 
     
     Args: 
          site (str): the url of the desired Footlocker page. 
          
     Returns: 
          A tuple of lists that contains details of the products on the page.
     """
     product_names = []
     product_gender = []
     product_colors = []
     product_prices = []
     
     #specify the url
     fl = "https://www.footlocker.com/category/mens/shoes.html"

     #query the site and return the html
     page = urllib.request.urlopen(fl)
     time.sleep(2)

     #parse the html
     soup = BeautifulSoup(page, "html.parser")

     for p in soup.find_all('span', class_='ProductName-primary'):
          product_names.append(p.text)
     
     for p in soup.find_all('span', class_='ProductName-alt'):
          gender = (re.search(r"(.*)•", p.text)).group(1)
          product_gender.append(gender)

     for p in soup.find_all('span', class_='ProductName-alt'):
          colors = (re.search(r"•(.*)", p.text)).group(1)
          product_colors.append(colors)
          
     for p in soup.find_all('span', class_='ProductPrice'):
          product_prices.append(float(p.text[1:]))
     
     return product_names, product_gender, product_colors, product_prices

class Shoe:
     """An object that represents features of a shoe on a store's site. 
     
     Attributes:
          name (str): the name of the shoe
          gender (str): the gender of the shoe
          color (str): the colors of the shoe
          price (float): the price of the shoe
     """
     name = ""
     gender = ""
     color = ""
     price = 0.0
     
     def __init__(self, name, gender, color, price):
          self.name = name
          self.gender = gender
          self.color = color
          self.price = price
          
