import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

url = 'https://parsinger.ru/selenium/5.7/1/index.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    divs = browser.find_elements(By.XPATH,'//*[@id="floating-container"]/div')
    for div in divs:
        button = div.find_element(By.TAG_NAME,"button")
        browser.execute_script("return arguments[0].scrollIntoView(true);", button)
        button.click()
    alert_text = browser.switch_to.alert.text
    print(alert_text)
    
