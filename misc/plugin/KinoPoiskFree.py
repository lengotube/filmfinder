from bs4 import BeautifulSoup
import requests

async def get_FilmsMe(name, web):
    url=f'https://www.kinopoisk.ru/index.php?kp_query={name}'
    request=requests.get(url)
    request.encoding = 'utf-8'
    soup=BeautifulSoup(request.text, "html.parser")
    id = soup.find(class_='element most_wanted').find(class_='pic').find('a')['data-id']
    name = soup.find(class_='element most_wanted').find(class_='pic').find('img')['alt']
    type_kino = soup.find(class_='element most_wanted').find(class_='pic').find('a')['data-type']
    link = f'{web}/{type_kino}/{id}'
    return link

