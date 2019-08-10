from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

option = webdriver.ChromeOptions()
option.add_argument(" - incognito")

location = input("Enter path for chrometools")

if len(location) == 0:
    location="/Users/mospy26/Documents/what-do-you-meme/chromedriver"

browser = webdriver.Chrome(executable_path=location, chrome_options=option)

try:
    element = WebDriverWait(browser, 100).until(
        EC.presence_of_element_located((By.ID, "select-text"))
    )
    print("Yes")
finally:
    browser.quit()
