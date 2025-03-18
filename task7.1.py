
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import json
url = 'https://parsinger.ru/selenium/7/7.1/index.html'


with webdriver.Chrome() as browser:
    browser.get(url)
    height = browser.execute_script("return document.body.scrollHeight")
    browser.execute_script(f"window.scrollBy(0,{height})")
    time.sleep(2)
    res = browser.find_element(By.ID,"secret-container").text
    print(res)
    time.sleep(5)
