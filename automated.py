
import urllib.request
from bs4 import BeautifulSoup
import time

#specify the url
fl = "https://www.footlocker.com/category/mens/shoes.html"

#query the site and return the html
page = urllib.request.urlopen(fl)
time.sleep(2)

#parse the html
soup = BeautifulSoup(page, "html.parser")

# for p in soup.find_all('span', class_='ProductName-primary'):
#     print(p.text)
   
# for p in soup.find_all('span', class_='ProductPrice'):
#     print(p.text)

for p in soup.find_all("a", class_="ProductCard-link ProductCard-content"):
     print(p.text)

