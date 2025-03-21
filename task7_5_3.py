import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
url = 'https://parsinger.ru/infiniti_scroll_2/'
with webdriver.Chrome() as browser:
    browser.get(url)
    action = ActionChains(browser)
    #div = browser.find_element(By.ID,"button-row")
    ar=[]
    el=1
    for i in range(10):
        div = browser.find_element(By.XPATH,'//*[@id="scroll-container"]/div')
        spans=browser.find_elements(By.TAG_NAME,"p")
        for span  in spans:
            if  span.text and span.text not in ar  and span.text.isdigit:
                ar.append(span.text)
                
            
            el+=1
        action.move_to_element(div).perform()
    print(sum(map(int,ar)))
    print(ar)
