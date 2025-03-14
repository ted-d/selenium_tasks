import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#поиск и клик по ссылке с получением текста 
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/2/2.html')
    link = browser.find_element(By.PARTIAL_LINK_TEXT, '16243162441624')
    if link:
        el = link.click()
        st = browser.find_element(By.ID,'result')
        print(st.text)
    time.sleep(5)
