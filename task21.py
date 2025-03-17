import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/scroll/4/index.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    buttons = browser.find_elements(By.CLASS_NAME,"btn")
    s=0
    for butt in buttons:
        browser.execute_script("return arguments[0].scrollIntoView(true);",butt)
        time.sleep(0.5)
        butt.click()
        
        s+=int(browser.find_element(By.ID,"result").text)

    
    
    
  
    print(s)
    time.sleep(5)
