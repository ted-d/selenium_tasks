import time
from selenium import webdriver
from selenium.webdriver.common.by import By
#добавляем куку на сайт 
url = 'https://parsinger.ru/selenium/6/6.3.3/index.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    browser.add_cookie({"name":"secretKey","value":"selenium123"})
    browser.refresh()
    
    res = browser.find_element(By.ID,"password").text
    print(res)
    time.sleep(5)
