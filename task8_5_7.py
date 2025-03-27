import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from math import sqrt 
#url = 'https://parsinger.ru/blank/3/index.html'
sites = ['http://parsinger.ru/blank/1/1.html', 'http://parsinger.ru/blank/1/2.html', 'http://parsinger.ru/blank/1/3.html',
         'http://parsinger.ru/blank/1/4.html', 'http://parsinger.ru/blank/1/5.html', 'http://parsinger.ru/blank/1/6.html',]
with webdriver.Chrome() as browser:
    ar=[]
    for url in sites:
        browser.switch_to.new_window('tab')
        browser.get(url)
        chb = browser.find_element(By.CLASS_NAME,'checkbox_class')
        chb.click()
        span = browser.find_element(By.ID,"result")
        ar.append(span.text)
    
    print(round(sum(map(sqrt,map(int,ar))),9))
    time.sleep(15)
    
