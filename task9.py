import time
from selenium import webdriver
from selenium.webdriver.common.by import By
#находим картинку по ID и делаем скриншот
url = 'https://parsinger.ru/selenium/6/6.2.1/index.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    browser.find_element(By.ID,"this_pic").screenshot('foo.jpg')
    time.sleep(5)
