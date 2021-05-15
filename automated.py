

import urllib.request
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re

class Data:
     def get_product_fl(links):
          """Takes a Footlocker web page as a parameter and returns the product
               details as a string. 
          
          Args: 
               links (list): a list of links of the shoes from the 
                    desired Footlocker page. 
               
          Returns: 
               A list of lists that contains details of the products on the page.
          """
          product_names = []
          product_gender = []
          product_colors = []
          product_prices = []
          product_description = []
          product_sizes = []
          product_num = []

          for link in links:
               #query the site and return the html
               page = urllib.request.urlopen(link)
               time.sleep(2)

               #parse the html
               soup = BeautifulSoup(page, "html.parser")

               try:
                    p = soup.find('span', class_='ProductName-primary')
                    product_names.append(p.text)
               except AttributeError:
                    continue
               
               try:
                    p = soup.find('span', class_='ProductName-alt')
                    product_gender.append(p.text)
               except AttributeError:
                    continue
               
               try:
                    p = soup.find('p', class_='ProductDetails-form__label')
                    product_colors.append(p.text)
               except AttributeError:
                    continue
               
               try:    
                    p = soup.find('span', class_='ProductPrice')
                    try:
                         product_prices.append(float(p.text[1:]))
                    except ValueError:
                         price = re.search(r"to \$(.*)\$.*\$", p.text).group(1)
                         product_prices.append(float(price))
               except AttributeError:
                    continue
               
               try:
                    p = soup.find('div', class_='ProductDetails-description')
                    product_description.append(p.text)
               except AttributeError:
                    continue
               
               try:      
                    p = soup.find('div', class_='ProductSize-group')
                    product_sizes.append(p.text)
               except AttributeError:
                    continue
               
               try:
                    p = soup.find('div', class_='Tab-panel')
                    number = re.search(r"#: (\w+\d\w*)", p.text).group(1)
                    product_num.append(number)
               except AttributeError:
                    continue
               
          
          return {"Name": product_names, "Gender": product_gender, 
                 "Colors: ": product_colors, "Price": product_prices,
                 "Description": product_description, "Sizes": product_sizes,
                 "Product ID": product_num}
          
          
     def get_product_link(site):
          """Takes a url for a page of products and returns a list of links
               of each specific product.
               
          Args:
               site (str): the url of the site page for links to be extracted.
               
          Returns:
               A list of links
          """
          list_links = []
          page = urllib.request.urlopen(site)
          time.sleep(2)
          
          #parse the html
          soup = BeautifulSoup(page, "html.parser")

          for p in soup.find_all("a", class_="ProductCard-link ProductCard-content"):
               list_links.append("https://www.footlocker.com" + p.get("href"))
          return list_links
          
     def scrape(url, PATH):
          """Uses Selenium to iterate through all pages of Footlocker's Men's shoes. 
               Calls the Data class from automated.py to store the data to a tuple. 
          
          Args:
               url (str): the url of the Footlocker website. 
               
          Returns:
               A list of links to each Men's shoe on the url page.
          """
          shoe_links = []
          state = True
          
          shoe_links.extend(Data.get_product_link(url))
          
          #PATH = "C:\Program Files (x86)\chromedriver.exe"
          driver = webdriver.Chrome(PATH)
          driver.get(url)
          
          time.sleep(1.5)
          try:
               driver.find_element_by_id("touAgreeBtn").click()
          except:
               pass
          time.sleep(3)
          webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
          
          i = 1
          while i < 3:#state == True:
               try:
                    i += 1
                    driver.find_elements_by_link_text(str(i))[0].click()
                    time.sleep(2)
                    new = driver.current_url
                    r = requests.get(new).url
                    shoe_links.extend(Data.get_product_link(r))
               except IndexError:
                    driver.close()
                    state = False

          return shoe_links

url = "https://www.footlocker.com/category/womens/shoes.html?currentPage=0"
# product = "https://www.footlocker.com/product/~/A5AO95KO.html"
# Data.get_product_fl([product])
# Data.get_product_link(url)
# s = Data.scrape(url)
# print(s[-1])
# print("len: ", len(s))
# Data.get_product_fl(s)
#Data.get_product_fl(["https://www.footlocker.com/product/birkenstock-arizona-womens/1019046B.html"])
