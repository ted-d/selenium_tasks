import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
url = 'https://parsinger.ru/selenium/9/9.4.4/index.html'
with webdriver.Chrome() as browser:
    
    browser.get(url)
    button=browser.find_element(By.CLASS_NAME,"btn")
    button.click()
    res=browser.current_url
    if WebDriverWait(browser,10).until(EC.url_changes(res)):
        res=browser.find_element(By.ID,"password")  
    print(res.text)
    time.sleep(1)
