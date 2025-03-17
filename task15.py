import time
from selenium import webdriver
from selenium.webdriver.common.by import By
#"sbisru-Header__menu-link sbis_ru-Header__menu-link sbisru-Header__menu-link--hover"
url = 'https://parsinger.ru/methods/1/index.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    el=None
    while True:
        browser.refresh()
        el = browser.find_element(By.ID,"result").text
        if el.isdigit():
            break
    print(el)        
    #browser.execute_script("return arguments[0].scrollIntoView(true);",element)
   # browser.find_element(By.ID,"target").click()
    #res = browser.find_element(By.ID,"secret-key").text
    #print(res)
    time.sleep(5)
