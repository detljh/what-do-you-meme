from bs4 import BeautifulSoup
import requests

r = requests.get("https://memeful.com/generator")
html_bytes = r.text

soup = BeautifulSoup(html_bytes, features="lxml")
search = soup.find("div", {'id': "search-div"})
