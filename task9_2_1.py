import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
url = 'https://parsinger.ru/selenium/9/9.2.1/index.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    button=WebDriverWait(browser,timeout=10).until(EC.element_to_be_clickable((By.TAG_NAME,'button')))
    button.click()
    res=''
    WebDriverWait(browser,timeout=20).until(EC.title_is(("Access Granted")))
    res = browser.find_element(By.ID,"passwordValue").text
    print(res)
    time.sleep(1)
    
