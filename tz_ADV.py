"""Сервис Wordstat. 
Страница: https://wordstat.yandex.ru/?region=all&view=graph&words=%D1%82%D0%B5%D1%81%D1%82 
* Для просмотра вы должны быть авторизованы в Яндексе

Нужно получить данные, указанные в прямоугольнике:
Из раздела “Динамика”
С разбивкой по дням
Результатом должен быть Excel-файл с колонками:
Фраза 
* На скриншоте фраза “тест”.
Дата
Число запросов

"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from openpyxl import Workbook
import os
chrome_options = Options()
chrome_options.add_argument(r"user-data-dir=C:\Users\Tony_Montana\AppData\Local\Google\Chrome\User Data")
chrome_options.add_argument("profile-directory=Profile 1")

# Дополнительные настройки
chrome_options.add_argument("--start-maximized")  # Открыть на полный экран
chrome_options.add_argument("--disable-extensions")  # Отключить расширения (опционально)

# Инициализация драйвера

url = 'https://wordstat.yandex.ru/?region=all&view=graph&words=%D1%82%D0%B5%D1%81%D1%82'

with webdriver.Chrome(options=chrome_options) as browser:
    ar=[]
    browser.get(url)
    text = browser.find_element(By.CLASS_NAME,"textinput__control")
    text=text.get_attribute("value")
    print(text)
    browser.find_element(By.CLASS_NAME,"Button2").click()  
    browser.find_element(By.CSS_SELECTOR,"[data-key='item-0']").click()
    buttons = browser.find_elements(By.CLASS_NAME,"rdp-cell")
    buttons[0].click()
    buttons[6].click()
    time.sleep(3)
    table= browser.find_elements(By.TAG_NAME,"td")
    data =[]
    ar=[]
    for row in table:
         if len(ar)<3:
            if len(row.text)>0: 
                ar.append(row.text)
            else:
                 break
         else:
            data.append(ar)
            ar=[]
            ar.append(row.text)
    wb = Workbook()
    ws = wb.active  
    ws['A1'] = f"На скриншоте фраза “{text}”" 
    ws.append([]) 
    headers = ["Дата", "Число запросов", "Доля от всех запросов"]
    ws.append(headers)



    for row in data:

        ws.append([row[0], row[1].replace(" ", "")]) 

# 5. Удаляем третий столбец (если он есть)
    ws.delete_cols(3)        
    filename = "wordstat_results.xlsx"
    wb.save(filename)
    print(f"Файл сохранен: {filename}")
