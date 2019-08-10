from bs4 import BeautifulSoup
import time
import requests

class NewsScraper():
    def __init__(self):
        url = "https://www.dailytelegraph.com.au/news/breaking-news"
        r = requests.get(url)
        data = r.text
        self.soup = BeautifulSoup(data,"lxml")
    
    def scrape_headline_title(self):
        title_text = self.soup.find_all("h2", {"class": "tge-cardv2_title"})
        return [i.text for i in title_text]

    def scrape_content(self):
        content_text = self.soup.find_all("p", {"class": "tge-cardv2_standfirst"})
        return [i.text for i in content_text]