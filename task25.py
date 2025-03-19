import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
url = 'https://parsinger.ru/selenium/7/7.3.1/index.html'
with webdriver.Chrome() as browser:
    browser.get(url)
      
    element = browser.find_element(By.ID,"draggable")
    
    action = ActionChains(browser)
    action.drag_and_drop_by_offset(element,0,-200).perform()
    password = browser.find_element(By.ID, "passwordContainer").text
    print("Пароль:", password)
