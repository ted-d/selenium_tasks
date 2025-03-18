import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = 'https://parsinger.ru/selenium/7/7.2/index.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    time.sleep(1)  
    list_input = []
    for _ in range(100):          
        inputs = browser.find_elements(By.CLASS_NAME, "input-wrapper")
        height =  browser.execute_script("return document.body.scrollHeight")        
        for input_field in inputs:
            input_element = input_field.find_element(By.TAG_NAME, "input")
            if input_element not in list_input:
                input_element.send_keys("abcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")  # Заполняем поле
                input_element.send_keys(Keys.ENTER)
                list_input.append(input_element)
                input_element.send_keys(Keys.ARROW_DOWN)
            else:
                browser.execute_script(f"window.scrollBy(0,{height})")       
        time.sleep(0.1)  

    
    password = browser.find_element(By.ID, "hidden-password").text
    print("Пароль:", password)
