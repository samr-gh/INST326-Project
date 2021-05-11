
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
          # fl = "https://www.footlocker.com/category/womens/shoes.html?currentPage=0"

          #query the site and return the html
          page = urllib.request.urlopen(site)
          time.sleep(2)

          #parse the html
          soup = BeautifulSoup(page, "html.parser")

          for p in soup.findAll('span', class_='ProductName-primary'):
               product_names.append(p.text)
          
          for p in soup.findAll('span', class_='ProductName-alt'):
               product_gender.append(p.text)

          for p in soup.findAll('div', class_='ProductDetails-form__info'):
               colors = (re.search(r'(.*)', p.text))
               product_colors.append(colors)
               
          for p in soup.findAll('span', class_='ProductPrice'):
                product_prices.append(float(p.text[1:]))
          
          for p in soup.findAll('div', class_='ProductDetails-description'):
               product_description.append(p.text)
     
          for p in soup.findAll('a', class_='bv-rating bv-text-link bv-popup-target bv-focusable'):
               product_rating.append(p.text)
               
          for p in soup.findAll('div', class_='ProductSize-group'):
               product_sizes.append(p.text)
          
          for p in soup.findAll('div', class_='Tab-panel'):
               number = (re.search(r"#:(.*) ", p.text)).group(1)
               product_num.append(number)
          
          for p in soup.findAll('span', class_='ProductName-primary'):
               brand = (re.search(r"/w+/s", p.text))
               product_brand.append(brand)
          
          print(product_names, product_gender, product_colors, product_prices, product_description, product_rating, product_sizes, product_num, product_brand)
          
          
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
Data.get_product_fl("https://www.footlocker.com/product/nike-air-force-1-07-le-low-womens/D8959100.html")

#get_product_fl()