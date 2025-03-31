import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
url = 'https://parsinger.ru/selenium/9/9.4.3/index.html'
with webdriver.Chrome() as browser:
    
    browser.get(url)
    buttons=browser.find_elements(By.CLASS_NAME,"btn")
    res=''
    for but in buttons:
        but.click()
        try:
            WebDriverWait(browser,10).until(EC.url_to_be("https://parsinger.ru/selenium/9/9.4.3/final.html?key=secure"))
            time.sleep(6.5)
            res=browser.find_element(By.ID,"password")
        except:
            browser.back()

    
   
    
    
    print(res.text)
    time.sleep(1)
