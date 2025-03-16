import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/6/6.3.2/index.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    cookies = browser.delete_all_cookies()
    time.sleep(15)
