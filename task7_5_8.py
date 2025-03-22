import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

url = 'https://parsinger.ru/selenium/5.7/4/index.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    browser.maximize_window()  # Максимизируем окно браузера
    ar = []  # Список для хранения уже обработанных чекбоксов

    # Находим главный контейнер
    mdiv = browser.find_element(By.XPATH, '//*[@id="main_container"]')

    # Устанавливаем фокус на главный контейнер
    action = ActionChains(browser)
    action.move_to_element(mdiv).perform()  # Перемещаем курсор к контейнеру
    print("Focus set on the main container")

    prev_count = 0  # Количество обработанных контейнеров на предыдущем шаге
    while True:
        # Находим все дивы внутри главного контейнера
        divs = mdiv.find_elements(By.TAG_NAME, "div")
        print(f"Found {len(divs)} divs")

        # Если количество контейнеров не изменилось, завершаем цикл
        if len(divs) == prev_count:
            break
        prev_count = len(divs)

        # Обрабатываем каждый див
        for div in divs:
            checkboxes = div.find_elements(By.CSS_SELECTOR, "[type='checkbox']")
            for ch in checkboxes:
                val = ch.get_attribute("value")
                if ch not in ar and val and val.isdigit() and int(val) % 2 == 0:
                    ch.click()
                    ar.append(ch)  # Добавляем чекбокс в список обработанных

        # Скроллим страницу вниз
        browser.execute_script("arguments[0].scrollTop += 500;", mdiv)  # Скроллим внутри контейнера
        print("Scrolled down by 500 pixels")

        # Ждем, чтобы новые элементы успели загрузиться
        time.sleep(1)

    # Кликаем на кнопку и получаем текст из alert
    browser.find_element(By.CLASS_NAME, "alert_button").click()
    alert_text = browser.switch_to.alert.text
    print("Alert text:", alert_text)
