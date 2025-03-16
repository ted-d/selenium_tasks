import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/6/6.5/index.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    element = browser.find_element(By.CLASS_NAME,"spacer")
    browser.execute_script("return arguments[0].scrollIntoView(true);",element)
    browser.find_element(By.ID,"target").click()
    res = browser.find_element(By.ID,"secret-key").text
    print(res)
    time.sleep(5)
