from bs4 import BeautifulSoup
import requests

class NewsScraper():
    def __init__(self):
        url = "https://www.dailytelegraph.com.au/news/breaking-news"
        r = requests.get(url)
        data = r.text
        self.soup = BeautifulSoup(data,"lxml")
    
    def scrape_headline_title(self):
        latest_news = self.soup.find("div", {"class": "tgs-mosaicv2-paddedcontainer"})
        new_soup = BeautifulSoup(latest_news.text, "lxml")
        title = list(map(lambda x: x.strip(), latest_news.text.replace("\t", " ").split("\n")))[1:][::3][:-1]
        return title

    def scrape_content(self):
        latest_news = self.soup.find("div", {"class": "tgs-mosaicv2-paddedcontainer"})
        new_soup = BeautifulSoup(latest_news.text, "lxml")
        content = list(map(lambda x: x.strip(), latest_news.text.replace("\t", " ").split("\n")))[2:][::3]
        return content

