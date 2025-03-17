
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
#"sbisru-Header__menu-link sbis_ru-Header__menu-link sbisru-Header__menu-link--hover"
url = 'https://parsinger.ru/selenium/5.5/1/1.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    blocks=browser.find_elements(By.CLASS_NAME,"text-field")
    for block in blocks:
        block.clear()
    browser.find_element(By.ID,"checkButton").click()
    alert = browser.switch_to.alert.text      
    #browser.execute_script("return arguments[0].scrollIntoView(true);",element)
   # browser.find_element(By.ID,"target").click()
    #res = browser.find_element(By.ID,"secret-key").text
    print(alert)
    time.sleep(5)
