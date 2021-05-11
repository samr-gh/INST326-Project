"""Talked to Instructor Cruz on April, 30 after discussion and he told us to 
    just have an outline of all of our functions and classes because we changed 
    our app functionality and he did not expect us to have functional code 
    written down. 
"""

import requests
import time
import csv
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from automated import Data

def scrape(url):
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
    
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get(url)
    time.sleep(4)
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    
    i = 1
    while state == True:
        try:
            i += 1
            print("loop " + str(i - 1))

            driver.find_elements_by_link_text(str(i))[0].click()
            time.sleep(2)
            new = driver.current_url
            r = requests.get(new).url
            print("R: " + r)
            shoe_links.extend(Data.get_product_link(r))
            print(len(shoe_links))
        except IndexError:
            driver.close()
            state = False

    return shoe_links

url = "https://www.footlocker.com/category/womens/shoes.html?currentPage=0"
scrape(url)

class Shoe:
     """An object that represents features of a shoe on Footlocker.  
     
     Attributes:
          name (str): the name of the shoe
          gender (str): the gender of the shoe
          color (str): the colors of the shoe
          price (float): the price of the shoe
          description (str): the description that Footlocker gives the shoe
          rating (float): the rating of the shoe based on reviews
          sizes (list): a list of floats representing the shoe sizes
          product_num (str): the unique product ID of the shoe
          brand (str): the brand of the shoe
     """
     def __init__(self, name, gender, color, price, description, rating, sizes, brand):
          self.name = name
          self.gender = gender
          self.color = color
          self.price = price
          self.description = description
          self.rating = rating
          self.sizes = sizes
          self.product_num = product_num
          self.brand = brand
              
     def __repr__(self):
        pass

def store_features(links):
    """Gets the attributes of a Shoe object from links of specific shoes
        and stores them in a new csv file.
    
    Args:
        links (list): a list of links returned by the scrape() function. 
        
    Returns:
        The csv file created. 
    """
    ada = {}
    for feature in get_product_fl:
        #ada.update(feature['product_names'])
        ada.add('Product Names', feature['product_names'])
        
    # for feature in get_product_fl:
    #     links = []
    #     links.append(feature['product_names'])
    #     links.append(feature.product_names)
    # print(links)
    
    #     links = []
    #     name = feature.find('name')
    #     gender = feature.find('gender')
    #     links.append((name, gender))
        
    df = pd.DataFrame(links, columns = [name])
    df.to_csv('shoe_attributes.csv', encoding='utf-8')
    

def print_features(shoe):
    """Takes a Shoe object and prints the attributes of it
    
    Args:
        shoe (Shoe object): the desired shoe
        
    No return
    """
    pass

def find_mean_price(brand):
    """Finds the mean price of a specific brand of shoe.
    
    Args:
        brand (str): the desired brand 
        
    Returns:
        A float value which is the mean price of all shoes of the brand. 
    """
    pass

def sort_rating(csv):
    """Sorts the shoes in the csv file from shoes with the highest to
        lowest rating. 
        
    Args:
        csv (csv file): the csv file created by the store_features()
            function. 
    
    Returns:
        A list of the ordered product numbers
    """
    pass

def similar_shoes(shoe):
    """Finds similar shoes that share at least 3 attributes of the given shoe
    
    Args:
        shoe (Shoe object): the shoe object returned by the main() function. 
        
    Returns:
        A list of shoe objects that match
    """
    pass

def main(criteria):
    """Takes criteria given by the user and suggests relevant shoes that 
        meet the criteria.
        
    Args: 
        criteria (str): the criteria given by the user (has some optional
            fields).
            
    Returns:
        The suggested shoe as a Shoe object
    """
    pass

def parse_args(args_list):
    """Create an instance of an ArgumentParser object and assigns one argument
        to it named "criteria" of type str. This argument accepts any number of
        command line arguments and creates a list of them. 
        
    Arguments: 
        args_list (list): a list of command line arguments (any length)
        
    Returns:
        ArgumentParser object created
    """
    pass

if __name__ == "__main__":
    pass
