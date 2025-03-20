from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/scroll/2/index.html')
    divs = browser.find_elements(By.CSS_SELECTOR, "[class='item']")
    ar=[]
    for div in divs:
        div.find_element(By.TAG_NAME,"input").click()
        span = div.find_element(By.TAG_NAME,"span").text
        if span is not None and span.isdigit():
            ar.append(span)
        span = None

    time.sleep(3)
    ar = list(map(int,ar))

    print(sum(ar))
