



from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import pandas as pd
import plotly.express as px



webpage = 'https://quotes.toscrape.com/'


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}


req = Request(webpage, headers = headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

print(soup.title.text + "\n")
