import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from math import sqrt 
url = 'https://parsinger.ru/selenium/5.8/5/index.html'

with webdriver.Chrome() as browser:
    ar=[]
    browser.get(url)
    iframes = browser.find_elements(By.TAG_NAME,"iframe")
    for frame in iframes:
        browser.switch_to.frame(frame)
        browser.find_element(By.TAG_NAME,"button").click()
        res = browser.find_element(By.TAG_NAME,"p").text
        browser.switch_to.default_content()
        browser.find_element(By.ID,"guessInput").send_keys(res)
        browser.find_element(By.TAG_NAME,"button").click()
        try:
            browser.switch_to.alert
            res = browser.switch_to.alert.text
            print(res)
            browser.switch_to.alert.accept()
            break
        except:
            pass
        try:
            browser.find_element(By.ID,"guessInput").clear()  
        except:
            pass  
    
    time.sleep(3)
    
