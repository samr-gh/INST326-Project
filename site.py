

from automated import Data


def store_features(links):
    """Gets the attributes of a shoe from its specific link
        and stores them in a new csv file.
    
    Args:
        links (list): a list of links returned by the scrape() function. 
        
    Returns:
        The csv file created. 
    """
    #     links = []
    #     links.append(feature['product_names'])
    #     links.append(feature.product_names)
    # print(links)
    
    #     links = []
    #     name = feature.find('name')
    #     gender = feature.find('gender')
    #     links.append((name, gender))
        
    # df = pd.DataFrame(links, columns = [name])
    # df.to_csv('shoe_attributes.csv', encoding='utf-8')
    pass

url = "https://www.footlocker.com/category/womens/shoes.html?currentPage=0"
links = Data.scrape(url)
store_features(links)

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

def main(criteria):
    """Takes criteria given by the user and suggests relevant shoes that 
        meet the criteria.
        
    Args: 
        criteria (str): the criteria given by the user (has some optional
            fields).
            
    Returns:
        The suggested shoe's attributes as a dictionary
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
