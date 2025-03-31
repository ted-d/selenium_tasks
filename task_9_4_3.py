import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
url = 'https://parsinger.ru/selenium/9/9.4.1/3VT6JyXnI7EQqG0632xSAQyD4Z.html'
with webdriver.Chrome() as browser:
    
    browser.get(url)
    while True:
        button=browser.find_element(By.ID,"searchLink")
        button.click()
        try :
            WebDriverWait(browser,5).until(EC.url_contains( "qLChv49"))
            res=browser.find_element(By.ID,"checkButton") 
            res.click()
            res = browser.find_element(By.ID,"result")
            print(res.text)
            break 
        except:
            pass 
