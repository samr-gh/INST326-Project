# import urllib.request
# response = urllib.request.urlopen('https://www.ebay.com')
# html = response.read()
# print(html)

import requests
from bs4 import BeautifulSoup

url = 'https://supremenewyork.com/checkout'
page = requests.get(url)
print(page)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='content')
print(results.prettify())
