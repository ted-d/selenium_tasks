import time
from selenium import webdriver
from selenium.webdriver.common.by import By
"""Числовая Сборка: Пройдитесь по всем 100 текстовым полям и соберите числа только из тех, которые имеют рядом "checked" чекбоксы."""
url = 'https://parsinger.ru/selenium/5.5/3/1.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    fields = browser.find_elements(By.CLASS_NAME,"parent")
    s=0
    for field in fields:
        ch = field.find_element(By.CLASS_NAME,"checkbox")
        if ch.is_selected():
            num = field.find_element(By.TAG_NAME,"textarea").text
            
            if num is not None and num.isdigit():
                s+=int(num)
    print(s)
    time.sleep(5)
