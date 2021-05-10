
"""This is code that was for a part of the project, but after talking with
Instructor Cruz we are taking a different approach and using Selenium. 
We are keeping this code here just in case as well to show the progress
that we had made before the change. 

Disregard this code. 
"""
import urllib.request
import requests
from bs4 import BeautifulSoup
import time
import re

class Data:
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
          product_description = []
          product_rating = []
          product_sizes = []
          product_num = []
          product_brand = []
          
          #specify the url
          #fl = "https://www.footlocker.com/category/womens/shoes.html?currentPage=0"

          #query the site and return the html
          page = urllib.request.urlopen(site)
          time.sleep(2)

          #parse the html
          soup = BeautifulSoup(page.text, "html.parser")

          for p in soup.findAll('span', class_='ProductName-primary'):
               product_names.append(p.text)
          
          for p in soup.findAll('span', class_='ProductName-alt'):
               gender = (re.search(r"(.*)•", p.text)).group(1)
               product_gender.append(gender)

          for p in soup.findAll('span', class_='ProductName-alt'):
               colors = (re.search(r"•(.*)", p.text)).group(1)
               product_colors.append(colors)
               
          for p in soup.findAll('span', class_='ProductPrice'):
               product_prices.append(float(p.text[1:]))
          
          for p in soup.findAll('meta', class_='content'):
               description(re.search(r"", p.text)).group(1)
          
          for p in soup.findAll('span', class_='bv-rating-stars-on bv-rating-stars bv-width-from-rating-stats-90'):
          
          for p in soup.findAll('span', class_='c-form-label-content'):
               product_sizes.append(p.text)
          
          for p in soup.findAll('span', class_='ProductID'):
          
          for p in soup.findAll('span', class_=''):
          
          print(product_names, product_gender, product_colors, product_prices)

     def get_product_link(site):
          list_links = []
          page = urllib.request.urlopen(site)
          #page = requests.get(site).url
          time.sleep(2)
          
          #parse the html
          soup = BeautifulSoup(page, "html.parser")

          for p in soup.find_all("a", class_="ProductCard-link ProductCard-content"):
               list_links.append("https://www.footlocker.com" + p.get("href"))
          return list_links
          
url = "https://www.footlocker.com/category/womens/shoes.html?currentPage=0"
Data.get_product_link(url)

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
          
#get_product_fl()