import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

url = 'https://parsinger.ru/selenium/8/8.2.2/index.html'
with webdriver.Chrome() as browser:
    ar=[]
    browser.get(url)
    d = browser.get_window_size()
    s = d['height']+d['width']
    browser.find_element(By.XPATH,"//*[@class='container']/input").send_keys(s)
    browser.find_element(By.CLASS_NAME,"container").find_element(By.ID,"checkBtn").click()

    res = browser.find_element(By.ID,"resultMessage").text
    res=res.split(": ")[1]
    print(res)
