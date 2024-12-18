import os.path
from bs4 import BeautifulSoup
import requests

from utils.files import save_site_to_file, read_site_from_file

name = "Гора%20в%20море"

url = "https://book24.ru"
search_url = "https://book24.ru/search/?q=" + name + "&by=desc&sort=sort"

headers = {
    'Accept': '*/*',
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 YaBrowser/24.12.0.0 Safari/537.36",
}

if not os.path.isfile('index.html'):
    response = requests.get(url=search_url, headers=headers)

    save_site_to_file('index.html', response.text)


src = read_site_from_file('index.html')

bs = BeautifulSoup(src, 'xlml')
bs.find()
