import time
from selenium import webdriver
from selenium.webdriver.common.by import By
#получаем куку с четным номером и сумируем ее значение
url = 'https://parsinger.ru/methods/3/index.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    cookies = browser.get_cookies()
    s=0
    for cook in cookies:
        ar=cook['name'].split("_")
        if ar[2].isdigit() and int(ar[2])%2==0:
            s+=int(cook['value'])

    
  
    print(s)
    time.sleep(5)
