import time
from selenium import webdriver
from selenium_stealth import stealth

browser = webdriver.Chrome()

stealth(browser,
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )


url = 'https://www.ozon.ru'


try:
    browser.get(url=url)
    time.sleep(10)
except Exception as e:
    print(e)
finally:
    browser.close()
    browser.quit()