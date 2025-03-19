
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
url = 'https://parsinger.ru/selenium/7/7.3.3/index.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    action = ActionChains(browser)
    action.key_down(Keys.CONTROL).key_down(Keys.ALT).key_down(Keys.SHIFT).send_keys('T').key_up(Keys.SHIFT).key_up(Keys.ALT).key_up(Keys.CONTROL).perform()
    password = browser.find_element(By.ID, "passwordContainer").text
    print("Пароль:", password)
