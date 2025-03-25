import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

url = 'https://parsinger.ru/selenium/8/8.4.2/index.html'
with webdriver.Chrome() as browser:
    ar=[]
    browser.get(url)
    for i in range(4):
        iframe = browser.find_element(By.TAG_NAME ,"iframe")
        browser.switch_to.frame(i)
        if i!=3:
            browser.find_element(By.TAG_NAME,"button").click()
        else:
            print(browser.page_source)
        browser.switch_to.default_content()

        time.sleep(3)
