import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/2/2.html')
    input_form = browser.find_elementы(By.TAG_NAME, 'a').send_keys('Text')
    time.sleep(5)
