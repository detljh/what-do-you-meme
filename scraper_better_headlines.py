from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time

option = webdriver.ChromeOptions()
option.add_argument(" - incognito")

location = input("Enter path for chrometools")

if len(location) == 0:
    location="/Users/mospy26/Documents/what-do-you-meme/chromedriver"

browser = webdriver.Chrome(executable_path=location, chrome_options=option)
browser.get("https://www.dailytelegraph.com.au/news/breaking-news")

time.sleep(2)

news_title = browser.find_elements(By.CLASS_NAME, "tge-cardv2_title")
news_content = browser.find_elements(By.CLASS_NAME, "tge-cardv2_standfirst")

print(len(news_title))
for i,j in zip(news_title, news_content):
    print(i.text)
    print(j.text)
    print("\n NEXT---> \n")
try:
    browser.quit()
    browser.close()
except:
    exit(0)
