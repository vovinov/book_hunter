import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium_stealth import stealth

from bs4 import BeautifulSoup

import requests

browser = webdriver.Chrome()

stealth(browser,
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )


def hunt_book(isbn, url):
    browser.get(url=url)
    time.sleep(2)
    input_text = browser.find_element(By.NAME, "text")
    input_text.clear()
    time.sleep(2)
    input_text.send_keys(isbn)
    input_text.send_keys(Keys.ENTER)

    return browser.current_url + '&sorting=price'


def get_price(site):

    request = requests.get(site)
    print(request)


if __name__ == "__main__":
    try:
        current_site = hunt_book("978-5-04-186916-8", 'https://www.ozon.ru')
        time.sleep(2)
        get_price(current_site)

    except Exception as e:
        print(e)

    finally:
        browser.close()
        browser.quit()
