import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#извлекаю все абзацы забираю оттуда текст и если число суммирую
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/3/3.html')
    tags = browser.find_elements(By.TAG_NAME, 'p')
    sum=0
    for p in tags:
        res = p.text
        if res is not None and res.isdigit():
            sum+=int(res)
    print(sum)
    time.sleep(5)
