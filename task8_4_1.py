#работиа с фремами 
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

url = 'https://parsinger.ru/selenium/8/8.4.1/'
with webdriver.Chrome() as browser:
    ar=[]
    browser.get(url)
    iframe = browser.find_element(By.TAG_NAME ,"iframe")
    browser.switch_to.frame(iframe)
    content = browser.page_source
    with open('text.csv','a',encoding = 'utf-8') as file:
        file.write(content)
#получил содержимое фрейма и записал в файл который буду обрабатывать в другом файле
with open('text.csv','r',encoding='utf-8') as file:
    ar=[]
    for i in file:
        if i.find("*")!=-1:
            l,r = i.find('*')+1,i.find('*')+2
            ar.append(i[l:r])
print("".join(ar))


