import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

url = 'https://parsinger.ru/selenium/8/8.1.2/index.html'
with webdriver.Chrome() as browser:
    ar=[]
    browser.get(url)
    
    links = browser.find_elements(By.XPATH,"//*[@class='code-links']/a")
    firtstdescr = browser.current_window_handle
    for _ in range(len(links)):
        browser.switch_to.window(firtstdescr)#каждую итерацию будет возвращаться на первую страницу 
        st = links[_].get_attribute("href")
        browser.switch_to.new_window('tab')   
        browser.get(st)
        time.sleep(3)
        nums = browser.find_element(By.CLASS_NAME,"numbers-container").find_elements(By.CLASS_NAME,"number")
        for num in nums:
            if num and num.text.isdigit():
                ar.append(num.text)
    browser.switch_to.window(firtstdescr)
    #browser.switch_to.new_window('tab')
    n = sum(list(map(int,ar)))
    time.sleep(5)
    browser.find_element(By.CLASS_NAME,"sum-check").find_element(By.ID,"sumInput").send_keys(n)
    browser.find_element(By.ID,"checkButton").click()
    res = browser.find_element(By.ID,"passwordDisplay").text
    res = res.split(": ")[1]

        
        
    
print(res)
