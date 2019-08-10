from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup
import urllib.request

class MemeScraper(object):
    def __init__ (self, url):
        self.url = "https://memeful.com/generator"

    def __repr__():
        return self.url
