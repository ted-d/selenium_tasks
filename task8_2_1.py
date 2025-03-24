import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

url = 'https://parsinger.ru/selenium/8/8.2.1/index.html'
with webdriver.Chrome() as browser:
    ar=[]
    browser.get(url)
    browser.set_window_size(1200,720)
    browser.find_element(By.ID,"checkSizeBtn").click()
    res = browser.find_element(By.ID,"secret").text
    
    print(res)
