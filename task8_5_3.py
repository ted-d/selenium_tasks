import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

url = 'https://parsinger.ru/selenium/5.8/3/index.html'
with webdriver.Chrome() as browser:
    ar=[]
    browser.get(url)
    buttons = browser.find_elements(By.CLASS_NAME ,"pin")
    check = browser.find_element(By.ID,"check")
    
    res=''
    for butt in buttons:
    
        st = butt.text
        check.click()
        time.sleep(0.2)
        browser.switch_to.alert.send_keys(st)
        browser.switch_to.alert.accept()
        time.sleep(0.3)
        
        res = browser.find_element(By.ID,"result")
        #res=browser.find_element(By.CLASS_NAME,"container").find_element(By.CLASS_NAME,"result-container").find_element(By.ID,"result")
        if res and res.text is not None:
            
            print(res.text)
