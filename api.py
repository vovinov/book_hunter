import time
from selenium import webdriver

options = webdriver.ChromeOptions
options.add_argument('user_agent=HelloWorld')
browser = webdriver.Chrome(options=options),


# url = 'https://www.ozon.ru'
url = 'https://www.whatismybrowser.com/detect/what-is-my-user-agent/'

try:
    browser.get(url=url)
    time.sleep(10)
except Exception as e:
    print(e)
finally:
    browser.close()
    browser.quit()