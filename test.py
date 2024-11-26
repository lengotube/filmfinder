from bs4 import BeautifulSoup
import requests
import asyncio
import re

async def search(name_film):
    url=f'https://www.kinopoisk.ru/index.php?kp_query={name_film}'
    request=requests.get(url)
    request.encoding = 'utf-8'
    soup=BeautifulSoup(request.text, "html.parser")
    print(soup)

asyncio.run(search('Человек паук паутина вселенных'))