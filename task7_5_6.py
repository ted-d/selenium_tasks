import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

url = 'https://parsinger.ru/selenium/5.7/5/index.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    buttons = browser.find_elements(By.XPATH,'//*[@id="main_container"]/button')
    action = ActionChains(browser)
    for button in buttons:
        action.click_and_hold(button).pause(float(button.text)+1).release().perform()
        
        
    alert_text = browser.switch_to.alert.text
    print(alert_text)
