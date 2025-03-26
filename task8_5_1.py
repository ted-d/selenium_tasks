import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

url = 'https://parsinger.ru/selenium/5.8/1/index.html'
with webdriver.Chrome() as browser:
    ar=[]
    browser.get(url)
    buttons = browser.find_elements(By.XPATH ,".//*[@class = 'container']/div/input")
    res=''
    for butt in buttons:
        if butt not in ar :
            butt.click()
            
            ar.append(butt)
            
            browser.switch_to.alert.accept()
            
            
            res=browser.find_element(By.CLASS_NAME,"container").find_element(By.CLASS_NAME,"result-container").find_element(By.ID,"result")
            if res.text is not None:
                res = res.text
                print(res)
           
    
    #browser.switch_to.default_content()

time.sleep(3)
    
