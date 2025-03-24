import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

url = 'https://parsinger.ru/selenium/8/8.3.1/index.html'
with webdriver.Chrome() as browser:
    ar=[]
    browser.get(url)
    browser.find_element(By.ID,"alertButton").click()
    browser.switch_to.alert.accept()
    time.sleep(1)
    browser.find_element(By.ID,"promptButton").click()
    browser.switch_to.alert.send_keys("Alert")
    browser.switch_to.alert.accept()
    time.sleep(1)
    browser.find_element(By.ID,"confirmButton").click()
    browser.switch_to.alert.accept()
    res=browser.find_element(By.ID,"secretKey").text
    print(res)
    time.sleep(10)
    
