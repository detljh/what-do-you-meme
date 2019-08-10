from bs4 import BeautifulSoup
import requests
import time

class KeywordScraper():
    def __init__(self, word):
        r = requests.get("https://relatedwords.org/relatedto/" + word)
        time.sleep(10)
        self.soup = BeautifulSoup(r.text)
        print(r.text)

    def scrape_keywords(self):
        filtered = self.soup.find_all("div", {'id': 'under-results'})
        #print(filtered)

s = KeywordScraper("crime")
s.scrape_keywords()
