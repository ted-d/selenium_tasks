from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/7/7.4.1/index.html')
    div = browser.find_element(By.CSS_SELECTOR, "[class='long-page']")
    ActionChains(browser).move_to_element(div).scroll_by_amount(1, 500).perform()
    time.sleep(3)
    res = browser.find_element(By.CSS_SELECTOR, "[class='countdown']").text
    res = res.split(": ")[1]
    #div = browser.find_element(By.CSS_SELECTOR,"[class='step_container']")
    ActionChains(browser).move_to_element(div).scroll_by_amount(1,1500).perform()
    time.sleep(1)
    browser.find_element(By.TAG_NAME,"input").send_keys(res)
    browser.find_element(By.TAG_NAME,"button").click()
    time.sleep(1)
    res = browser.find_element(By.ID,"final-key").text
    print(res)
