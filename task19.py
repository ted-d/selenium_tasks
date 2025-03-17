import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/5.5/2/1.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    blocks = browser.find_elements(By.CLASS_NAME,"text-field")
    s=0
    for block in blocks:
        if not block.get_attribute('disabled'):
            block.clear()

    browser.find_element(By.ID,"checkButton").click()
    alert = browser.switch_to.alert.text
    
  
    print(alert)
    time.sleep(5)
