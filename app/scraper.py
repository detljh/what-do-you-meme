from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time

class NewsScraper():
    def __init__(self):
        self.driver_location = "../venv/chromedriver"
        self.browser = "https://www.dailytelegraph.com.au/news/breaking-news"
    
    def scrape_headline_and_content(self):
        option = webdriver.ChromeOptions()
        option.add_argument(" - incognito")
        self.driver = webdriver.Chrome(executable_path=self.driver_location, chrome_options=option)
        self.driver.get(self.browser)
        time.sleep(3)
        news_title = self.driver.find_elements(By.CLASS_NAME, "tge-cardv2_title")
        news_content = self.driver.find_elements(By.CLASS_NAME, "tge-cardv2_standfirst")
        return (news_title, news_content) 

    def close(self):
        time.sleep(1)
        self.driver.close()

scraper = NewsScraper()
title, content = scraper.scrape_headline_and_content()
for i in zip(title, content):
    print(i[0].text, i[1].text)

scraper.close()

# option = webdriver.ChromeOptions()
# option.add_argument(" - incognito")

# location = input("Enter path for chrometools")

# if len(location) == 0:
#     location="venv/chromedriver"

# browser = webdriver.Chrome(executable_path=location, chrome_options=option)
# browser.get("https://www.dailytelegraph.com.au/news/breaking-news")

# time.sleep(2)

# news_title = browser.find_elements(By.CLASS_NAME, "tge-cardv2_title")
# news_content = browser.find_elements(By.CLASS_NAME, "tge-cardv2_standfirst")

# print(len(news_title))
# for i,j in zip(news_title, news_content):
#     print(i.text)
#     print(j.text)
#     print("\n NEXT---> \n")
# try:
#     browser.quit()
#     browser.close()
# except:
#     exit(0)
