import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#суммирую значение каждого 2-го вхождения тэга 
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/3/3.html')
    tags = browser.find_elements(By.XPATH, "//div[@class='text']/p[2]")
    sum=0
    for p in tags:
        res = p.text
        if res is not None and res.isdigit():
            sum+=int(res)
    print(sum)
    time.sleep(5)
