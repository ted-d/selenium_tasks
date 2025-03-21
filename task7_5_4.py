import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

url = 'https://parsinger.ru/infiniti_scroll_3/'
with webdriver.Chrome() as browser:
    browser.get(url)
    action = ActionChains(browser)
    ar = []

    # Обрабатываем каждый блок
    for i in range(1, 6):  # Блоки с 1 по 5
        # Находим контейнер блока
        div = browser.find_element(By.XPATH, f'//*[@id="scroll-wrapper_{i}"]/div')
        
        # Прокручиваем блок и собираем данные
        for _ in range(100):  # Прокручиваем 10 раз (можно увеличить, если нужно)
            # Находим все <span> внутри текущего блока
            spans = div.find_elements(By.TAG_NAME, "span")
            for span in spans:
                text = span.text
                if text and text.isdigit() and text not in ar:
                    ar.append(text)
            
            # Прокручиваем блок вниз на 150px (5 элементов по 30px)
            browser.execute_script("arguments[0].scrollBy(0, 30);", div)
            

    # Преобразуем строки в числа и суммируем
    print(sum(map(int, ar)))
    print(ar)
