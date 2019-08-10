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
browser.get("https://www.reuters.com/news/archive/worldNews?date=today")

time.sleep(2)

news_photo = browser.find_elements(By.CLASS_NAME, "story-photo")
news_title = browser.find_elements(By.CLASS_NAME, "story-title")
news_content = browser.find_elements(By.TAG_NAME, "p")


for i,j in zip(news_title, news_content):
    print(i.text)
    print("\n")
    print(j.text)
    print("\n NEXT---> \n")
try:
    browser.quit()
    browser.close()
except:
    exit(0)
os.system("taskkill chrome.exe")
