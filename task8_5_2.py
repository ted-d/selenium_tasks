import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

url = 'https://parsinger.ru/selenium/5.8/2/index.html'
with webdriver.Chrome() as browser:
    ar=[]
    browser.get(url)
    buttons = browser.find_elements(By.CLASS_NAME ,"buttons")
    inp = browser.find_element(By.ID ,"input")
           
    chbut = browser.find_element(By.CLASS_NAME,"res").find_element(By.ID,"check")
    res=''
    for butt in buttons:
        if butt not in ar :
            butt.click()
            
            ar.append(butt)
            time.sleep(0.2)
            res = browser.switch_to.alert.text

            browser.switch_to.alert.accept()
            time.sleep(0.3)
            inp.send_keys(res)
            chbut.click()
            res = browser.find_element(By.ID,"result")
            #res=browser.find_element(By.CLASS_NAME,"container").find_element(By.CLASS_NAME,"result-container").find_element(By.ID,"result")
            if res and res.text is not None:
                
                print(res.text)
           
    
    #browser.switch_to.default_content()

time.sleep(3)
    

    
