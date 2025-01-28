from time import sleep
from selenium import webdriver
from dotenv import load_dotenv
import os

load_dotenv()

browser = webdriver.Chrome()
browser.implicitly_wait(5)

browser.get('https://www.instagram.com/')




browser.close()