import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#выбор всех числовых значений из выпадающего списка и их суммирование
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/7/7.html')
    tags = browser.find_elements(By.TAG_NAME, "option")
    s=0
    for p in tags:
        val = p.text
        if val is not None and val.isdigit():
            s+=int(val)
    browser.find_element(By.ID,"input_result").send_keys(s)
    browser.find_element(By.ID,"sendbutton").click()
    res = browser.find_element(By.ID,"result")
    print(res.text)
    time.sleep(5)
