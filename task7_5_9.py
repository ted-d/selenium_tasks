import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

url = 'https://parsinger.ru/selenium/7/7.5/index.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    browser.maximize_window()  # Максимизируем окно браузера
    ar = []  # Список для хранения уже обработанных спанов

    # Находим главный контейнер
    mdiv = browser.find_element(By.XPATH, '//*[@id="container"]')

    # Устанавливаем фокус на главный контейнер
    action = ActionChains(browser)
    action.move_to_element(mdiv).perform()  # Перемещаем курсор к контейнеру
    
    s=0
    prev_count = 0  # Количество обработанных контейнеров на предыдущем шаге
    while True:
        # Находим все дивы внутри главного контейнера
        divs = mdiv.find_elements(By.CLASS_NAME, "card")
        

        # Если количество контейнеров не изменилось, завершаем цикл

        if len(divs) == prev_count:
            break
        prev_count = len(divs)
        # Обрабатываем каждый див
        for div in divs:
            
            span = div.find_element(By.CLASS_NAME, 'info').find_element(By.XPATH,".//*[@class='like-container']/span[@class='like-btn']")#точка позволят искать/
          #не по всей странице
            if span not in ar and  span.is_displayed() and span.is_enabled():
                ar.append(span)
                span.click() #после клика спанклик пропадает поэтому чтобы не кликать по существующему спану надо его в лист добавлять и проверять наличие
                num = div.find_element(By.XPATH,".//*[@class='number-wrapper']/span")
                if num not in ar and  num and num.text.isdigit() :
                    s+=int(num.text)  

            # Скроллим страницу вниз
        browser.execute_script("arguments[0].scrollTop += 500;", mdiv) # Скроллим внутри контейнера
    
    print(s)

    # Ждем, чтобы новые элементы успели загрузиться
    time.sleep(1)

    
