import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
url = 'https://parsinger.ru/selenium/9/9.1.1/index.html'
with webdriver.Chrome() as browser:
    
    
    browser.get(url)
    divs = browser.find_element(By.CLASS_NAME,"button-container").find_elements(By.TAG_NAME,"div")
    for div in divs:
        element=WebDriverWait(div,15).until(EC.element_to_be_clickable((By.TAG_NAME,"button")))
        element.click()
        
    #browser.find_element(By.TAG_NAME,"button").click()
    res = browser.find_elements(By.TAG_NAME,"p")
    time.sleep(5)
    print(res[0].text,res[-1].text)
