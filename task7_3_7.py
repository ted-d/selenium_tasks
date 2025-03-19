#правый клик по объекту и использование поиска по css selectору
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
url = 'https://parsinger.ru/selenium/7/7.3.4/index.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    action = ActionChains(browser)
    action.context_click(browser.find_element(By.ID,"context-area")).perform()
    time.sleep(4)
    browser.find_element(By.CSS_SELECTOR,"[data-action='get_password']").click()
    res = browser.find_element(By.CSS_SELECTOR,"[key='access_code']").text
    
    print("Пароль:", res)
