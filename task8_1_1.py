import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

url = 'https://parsinger.ru/selenium/7/7.5/index.html'
with webdriver.Chrome() as browser:
    ar=[]
    browser.get("about:blank")
    browser.switch_to.new_window("tab")
    browser.get("https://parsinger.ru/selenium/8/8.1/site1/")
    num1 = browser.title.replace('4','').replace('3','').replace('9','')
    ar.append(int(num1))
    browser.switch_to.new_window('tab')
    browser.get('https://parsinger.ru/selenium/8/8.1/site2/')
    num2 = browser.title.replace('7','').replace('8','').replace('0','')
    ar.append(int(num2))
print(sum(ar))
