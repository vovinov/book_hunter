import time
from selenium import webdriver

browser = webdriver.Chrome()

url = 'https://www.ozon.ru'

try:
    browser.get(url=url)
    time.sleep(10)
except Exception as e:
    print(e)
finally:
    browser.close()
    browser.quit()