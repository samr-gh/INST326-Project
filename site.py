

from automated import Data
import pandas as pd
from argparse import ArgumentParser
import sys

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
    

def print_features(dict):
    """Takes a shoe and prints the attributes of it
    
    Args:
        dict (dictionary): holds the attributes of the desired shoe
        
    No return
    """
    pass

# def find_mean_price(brand):
#     """Finds the mean price of a specific brand of shoe.
    
#     Args:
#         brand (str): the desired brand 
        
#     Returns:
#         A float value which is the mean price of all shoes of the brand. 
#     """
#     pass

# def sort_rating(csv):
#     """Sorts the shoes in the csv file from shoes with the highest to
#         lowest rating. 
        
#     Args:
#         csv (csv file): the csv file created by the store_features()
#             function. 
    
#     Returns:
#         A list of the ordered product numbers
#     """
#     pass

# def similar_shoes(shoe, data):
#     """Finds similar shoes that share at least 3 attributes of the given shoe
    
#     Args:
#         shoe (dictionary): the shoe's features returned by the main() function. 
#         data (csv): the csv storing the shoe data
        
#     Returns:
#         A list of shoe objects that match
#     """
#     pass

def find_shoe(attributes, csv):
    """Takes some attributes and the csv file created by the store_features()
        function and finds the shoe or shoes that mention the attributes the 
        most on its product page. 
        
    Args:
        attributes (list): a list of the attributes given by the user.
        csv (csv file): the csv file created by the store_features function.
        
    Returns:
        A string representing the modified product ID of the shoe, 
            or shoes if the number of matching instances is a tie.
    """
    list_counts = []
    for line in csv:
        count = 0
        for word in line:
            for i in attributes:
                if word == attributes[i]:
                    count += 1
        list_counts.append(count)

def main(criteria):
    """Takes criteria given by the user and suggests relevant shoes that 
        meet the criteria.
        
    Args: 
        criteria (list): the criteria given by the user (has some optional
            fields).
            
    Returns:
        The suggested shoe's attributes as a dictionary
    """
    if(criteria[0] == "M"):
        a = Data.scrape("https://www.footlocker.com/category/mens/shoes.html?currentPage=0")
    elif(criteria[0] == "W"):
        a = Data.scrape("https://www.footlocker.com/category/womens/shoes.html?currentPage=0")
    else:
        print("Please choose either 'M' or 'W'")
    #print(type(criteria[0]))
    #print(a)

def parse_args(args_list):
    """Create an instance of an ArgumentParser object and assigns two arguments
        to it named "gender" and "attributes" of type str. 
        
    Arguments: 
        args_list (str): the command line arguments 
        
    Returns:
        A list of the two arguments from the ArgumentParser object created.
    """
    parser = ArgumentParser(description = "Take a page and some attributes.")
    parser.add_argument("--gender", type = str)
    parser.add_argument("--attributes", type = str, nargs = "+")
    p = parser.parse_args(args_list)
    #print(p.gender)
    return [p.gender, p.attributes]
    

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args)
