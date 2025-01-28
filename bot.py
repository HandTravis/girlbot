from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
import os

load_dotenv()

username = os.getenv('INSTA_USERNAME')
password = os.getenv('INSTA_PASSWORD')

browser = webdriver.Chrome()
browser.implicitly_wait(5)

browser.get('https://www.instagram.com/')
user_link = browser.find_element(By.NAME, 'username')
password_link = browser.find_element(By.NAME, 'password')

user_link.click()
user_link.send_keys(username)

password_link.click()
password_link.send_keys(password)
password_link.send_keys(Keys.RETURN)

sleep(15)



browser.close()