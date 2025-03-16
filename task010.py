import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/6/6.3.1/index.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    cookie = browser.get_cookie('token_22')['value']
    print(cookie)
    time.sleep(5)
