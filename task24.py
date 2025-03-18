from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
url = 'https://parsinger.ru/methods/3/index.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    cookies = browser.get_cookies()
    s=0
    for cook in cookies:
        if 'secret_cookie_' in cook['name']:
            if cook['value'] is not None and cook['value'].isdigit():
                s+=int(cook['value'])
        
    print(s)
    time.sleep(5)
