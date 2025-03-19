# Задача: прокрутить оба контейнера до конца и считать пароль.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
url = 'https://parsinger.ru/selenium/7/7.3.5/index.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    l_container = browser.find_element(By.ID,"scrollable-container-left")
    action = ActionChains(browser)
    action.click(l_container).perform()
    while True:
        action.send_keys(Keys.END).perform()
        if browser.find_element(By.ID,"status-left").text!="Статус: не прокручено":
            break
    r_container = browser.find_element(By.ID,"scrollable-container-right")
    action.click(r_container).perform()
    while True:
        action.send_keys(Keys.END).perform()
        if browser.find_element(By.ID,"status-right").text!="Статус: не прокручено":
            break
    key= browser.find_element(By.CSS_SELECTOR,"[key='access_code']").text
    print(key)
