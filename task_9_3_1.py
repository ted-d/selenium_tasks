import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
url = 'https://parsinger.ru/selenium/9/9.3.1/index.html'
with webdriver.Chrome() as browser:
    browser.implicitly_wait(10)
    browser.get(url)
    button=browser.find_element(By.ID,"startButton")
    button.click()
    for _ in range(5):
        browser.find_element(By.ID,"dynamicButton").click()
    
    res=''
    
    res = browser.find_element(By.ID,"secretPassword").text
    print(res)
    time.sleep(1)
    
