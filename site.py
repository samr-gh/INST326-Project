"""This script deals with the functional printing of information of our program
"""

from automated import Data
import pandas as pd
from argparse import ArgumentParser
import sys
import csv


def store_features(shoe_dict):
    """Takes a dictionary with the attributes of shoes returned from 
        get_product_fl() from the Data class. Creates a csv file storing them.
    
    Args:
        shoe_dict (dict): a dictionary with keys as different attributes of shoes
            and values of lists returned by the get_product_fl() function. 
        
    No return 
    """
    #Source 1
    df = pd.DataFrame.from_dict(shoe_dict)
    #Source 2
    csv = df.to_csv("shoe_attributes.csv")
    

def find_shoe(attributes):
    """Takes some attributes and the csv file created by the store_features()
        function and finds the shoe or shoes that mention the attributes the 
        most on its product page. 
        
    Args:
        attributes (list): a list of the attributes given by the user.
        
    Prints:
        A list containing the attributes of the first shoe
            found with the highest count. 
    """
    list_counts = []
    
    with open("shoe_attributes.csv", encoding = "utf-8") as f:
        for line in f:
            lower_line = line.lower()
            inst = 0
            count = len(attributes) - 1
            while count >= 0:
                if attributes[count] in lower_line:
                    inst += lower_line.count(attributes[count])
                count -= 1
            list_counts.append(inst)
        winner = list_counts.index(max(list_counts))
    #Source 4
    with open("shoe_attributes.csv", encoding = "utf-8") as csv_file:
        reader = csv.reader(csv_file)
        rows = list(reader)
    
    print(rows[winner])
    
    
def main(criteria):
    """Takes criteria given by the user and suggests relevant shoes that 
        meet the criteria.
        
    Args: 
        criteria (list): the criteria given by the user (has some optional
            fields).
            
    No return
    """
    if(criteria[0] == "M"):
        shoe_links = Data.scrape("https://www.footlocker.com/category/mens/shoes.html?currentPage=0", criteria[2])
    elif(criteria[0] == "W"):
        shoe_links = Data.scrape("https://www.footlocker.com/category/womens/shoes.html?currentPage=0", criteria[2])
    else:
        print("Please select a gender by choosing either 'M' or 'W'")
        
    shoe_dict = Data.get_product_fl(shoe_links)
    store_features(shoe_dict)
    find_shoe(criteria[1])
    

def parse_args(args_list):
    """Create an instance of an ArgumentParser object and assigns two arguments
        to it named "gender" and "attributes" of type str. 
        
    Arguments: 
        args_list (str): the command line arguments 
        
    Returns:
        A list of the two arguments from the ArgumentParser object created.
    """
    #Source 3
    parser = ArgumentParser(description = "Take a page and some attributes.")
    parser.add_argument("--gender", type = str)
    parser.add_argument("--attributes", type = str, nargs = "+")
    parser.add_argument("--PATH", type = str)
    p = parser.parse_args(args_list)
    
    return [p.gender, p.attributes, p.PATH]
    

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args)
