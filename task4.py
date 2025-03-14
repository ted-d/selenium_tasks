import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#включение чекбоксов после нажатие кнопки и получение текста 
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/4/4.html')
    tags = browser.find_elements(By.XPATH, "//div[@class='content']/input")
    
    for p in tags:
        p.click()
    browser.find_element(By.CLASS_NAME,"btn").click()
    res = browser.find_element(By.ID,"result")
    print(res.text)
    time.sleep(5)
