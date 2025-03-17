"""


    Загрузка Страницы: Откройте страницу с помощью Selenium. 

        Используйте эту страницу с двумя элементами для тренировки.

    Коды Цветов: Получите цвет в формате HEX из каждого элемента <span>.

    Выбор в Списке: В выпадающем списке в каждом контейнере найдите и выберите тот же HEX цвет что и у родительского контейнера.

    Кнопочная Магия: Найдите и нажмите на кнопку, у которой атрибут data-hex совпадает с HEX цветом родительского контейнера.

    Чек-Бокс Челлендж: Поставьте галочку в чек-боксе на странице.

    Текстовое Поле: Вставьте в текстовое поле тот же HEX-цвет, который имеет фон родительского контейнера.

    Подтверждение: Нажмите на кнопку "Проверить": если вставлен корректный HEX, то на кнопке появится "ОК".

    Повторение: Повторите все эти шаги для каждого найденного на странице контейнера.

    Финальный Шаг: После выполнения всех действий, нажмите на кнопку "Проверить все элементы", кнопка расположена в самом низу, появится alert если все условия соблюдены.

    Секретный Код: Из алерт-окна получите числовой код и вставьте его в поле ответа степик.

"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
url = 'https://parsinger.ru/selenium/5.5/5/1.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    divs = browser.find_elements(
        By.XPATH,
        '//div[contains(@style, "background-color") and contains(@style, "width: 100%")]'
    )
    n=0
    for elm in divs:
        
        span = elm.find_element(By.TAG_NAME,"span").text#1-st span
        dropd = elm.find_element(By.TAG_NAME,"select")
        sel = Select(dropd)
        sel.select_by_visible_text(str(span))
        buttons = elm.find_elements(By.TAG_NAME,"button")
        chbs = elm.find_elements(By.TAG_NAME,"input")
        for chb in chbs:
            if chb.get_attribute("type")=="checkbox":
                chb.click()
            else:
                chb.send_keys(span)
        for butt in buttons:
            if butt.get_attribute("data-hex")==span:
                butt.click()
        button = elm.find_element(By.XPATH, '//button[text()="Проверить"]')
        button.click()
        
    browser.find_element(By.XPATH, '//button[text()="Проверить все элементы"]').click()
    alert = browser.switch_to.alert.text
    print(alert)
        
       
    time.sleep(5)
