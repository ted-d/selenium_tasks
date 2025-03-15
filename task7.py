
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select  # Импортируем класс Select


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/6/6.html')
    
    # Ваш код для вычисления значения
    tags = browser.find_elements(By.CLASS_NAME, "num")
    s = 0
    st = ''
    for tag in tags:
        st += tag.text
        st += '*'
    st = st.replace("((", '')
    st = list(map(lambda x: x.split("*"), st.split(")")))
    st = int(st[0][0]) * int(st[0][1]) * int(st[1][1]) + int(st[2][1])
    
    # Находим выпадающий список
    dropdown = browser.find_element(By.ID, "selectId")  
    select = Select(dropdown)  
    
    # Выбираем опцию по значению
    #select.select_by_value(str(st))  # Выбираем опцию по значению (значение должно быть строкой)
    
    # Или можно выбрать по видимому тексту
    select.select_by_visible_text(str(st))
    
    # Или по индексу
    # select.select_by_index(индекс)

    browser.find_element(By.ID, "sendbutton").click()
    res = browser.find_element(By.ID, "result")
    print(res.text)
    time.sleep(5)
