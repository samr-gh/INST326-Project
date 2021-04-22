
import urllib.request
from bs4 import BeautifulSoup

def scrape(site):
    """Scrapes a website for the required information needed to checkout.
    
    Args:
        site(Site object): a website object taken from a store's website. 
        
    Returns:
        List of data required for checking out. 
    """
    
#specify the url
fl = "https://www.footlocker.com/checkout"

#query the site and return the html
page = urllib.request.urlopen(fl)

#parse the html
soup = BeautifulSoup(page, "html.parser")

