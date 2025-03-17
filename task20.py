import time
from selenium import webdriver
from selenium.webdriver.common.by import By
'''

Следование за линками: На основной странице будет 42 ссылки. Открывайте каждую из них, чтобы исследовать и выяснить, какой из cookies имеет самый долгий срок жизни.

Вычисление жизнеспособности: Для каждой открытой страницы анализируйте срок жизни её cookie ['expiry']. Сохраняйте эти данные для последующего сравнения.

Коронация Бессмертного: После проверки всех 42 страниц определите, на какой из них находится cookie с самым долгим сроком жизни. С этой страницы извлеките число которое лежит в  теге <p id="result">INT</p>.

Завершающий этап: Вставьте полученное число в специальное поле для степик. Поздравляем, вы нашли "Бессмертного Печенюшка" и преуспели в этой миссии!
'''
url = 'https://parsinger.ru/methods/5/index.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    blocks = browser.find_elements(By.CLASS_NAME,"urls")
    d = {}
    for block in blocks:
        block.find_element(By.TAG_NAME,"a").click()

        cookies = browser.get_cookies()
        for cook in cookies:
            id = browser.find_element(By.ID,"result").text
            d[id]=cook['expiry']
        browser.back()



    mcook = max(d,key=lambda x: int(d[x]))
    
    
  
    print(mcook)
    time.sleep(5)
