import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/6/6.2/index.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    for i in range(2):
        browser.find_element(By.TAG_NAME,"a").click()
    browser.back()
    browser.back()
    browser.find_element(By.ID,"getPasswordBtn").click()
    time.sleep(5)
