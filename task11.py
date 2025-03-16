import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/6/6.3/index.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    cookies = browser.get_cookies()
    song = ''
    for cookie in cookies:
        song=cookie['name']
    browser.find_element(By.ID,"phraseInput").send_keys(song)
    browser.find_element(By.ID,"checkButton").click()
    res = browser.find_element(By.ID,"result").text
    print(res)
    time.sleep(5)
