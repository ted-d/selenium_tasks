import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

url = 'https://parsinger.ru/selenium/8/8.4.3/index.html'
with webdriver.Chrome() as browser:
    ar=[]
    browser.get(url)
    iframe = browser.find_element(By.TAG_NAME ,"iframe")
    browser.switch_to.frame(iframe)
    browser.find_element(By.TAG_NAME,"button").click()
    iframe = browser.find_element(By.TAG_NAME ,"iframe")
    browser.switch_to.frame(iframe)
    browser.find_element(By.TAG_NAME,"button").click()
    iframe = browser.find_element(By.TAG_NAME ,"iframe")
    browser.switch_to.frame(iframe)
    browser.find_element(By.TAG_NAME,"button").click()
    iframe = browser.find_element(By.TAG_NAME ,"iframe")
    browser.switch_to.frame(iframe)
    browser.find_element(By.TAG_NAME,"button").click()
    print(browser.page_source)
    #browser.switch_to.default_content()

    time.sleep(3)
