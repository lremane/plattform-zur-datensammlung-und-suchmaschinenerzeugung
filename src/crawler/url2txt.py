import requests
from bs4 import BeautifulSoup

URL = "https://www.wikidata.org/wiki/Q2079"
page = requests.get(URL)
print(page.text)
