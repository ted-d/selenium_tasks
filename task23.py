import time
from selenium import webdriver
from selenium.webdriver.common.by import By
#Миссия "Синхронизация": На странице находятся 100 текстовых полей: 50 серых и 50 синих. Ваша задача — перенести числа из серых полей в синие.
url = 'https://parsinger.ru/selenium/5.5/4/1.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    fields = browser.find_elements(By.CLASS_NAME,"parent")
    s=0
    gr=0
    for field in fields:
        textareas = field.find_elements(By.TAG_NAME,"textarea")
        for area in textareas:
        
            if area.get_attribute("color")=="gray":
                gr=int(area.text)
                area.clear()
                
            else:
                area.send_keys(gr)
                gr=''
        field.find_element(By.TAG_NAME,"button").click()
            
    browser.find_element(By.ID,"checkAll").click()
    res = browser.find_element(By.ID,"congrats").text
    print(res)
       
    time.sleep(5)
