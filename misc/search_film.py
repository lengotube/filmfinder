from bs4 import BeautifulSoup
import requests
import re

def spisok_number_to60():
    counter_number=int()
    list_rt=str()
    while counter_number != 60:
        counter_number+=1
        list_rt+=f'{str(counter_number)} '
    list_rt=list_rt.split()
    return list_rt

async def search(name_film):
    url=f'https://www.kinopoisk.ru/index.php?kp_query={name_film}'
    request=requests.get(url)
    request.encoding = 'utf-8'
    soup=BeautifulSoup(request.text, "html.parser")
    a = soup.find(class_='element most_wanted').find(class_='pic').find('a')['data-url']
    id = soup.find(class_='element most_wanted').find(class_='pic').find('a')['data-id']
    name = soup.find(class_='element most_wanted').find(class_='pic').find('img')['alt']
    year = soup.find(class_='element most_wanted').find(class_='year').get_text()
    type_kino = soup.find(class_='element most_wanted').find(class_='pic').find('a')['data-type']
    photo = f'https://st.kp.yandex.net/images/film_iphone/iphone360_{id}.jpg'
    genre = soup.find(class_='element most_wanted').find(class_='info').find_all(class_='gray')[1].get_text().split('\n')[1]
    director = soup.find(class_='element most_wanted').find(class_='info').find_all(class_='gray')[1].get_text().split('\n')[0]
    text_autor = soup.find(class_='element most_wanted').find(class_='info').find_all(class_='gray')[2].get_text()
    length = soup.find(class_='element most_wanted').find(class_='info').find(class_='gray').get_text()

    class rt_films_data():
        id_ = id
        name_film_=name
        year_ = year
        type_kino_='Фильм' if type_kino == 'film' else 'Сериал'
        genre_=genre
        photo_=photo
        director_=director
        text_autor_=text_autor
        length_=re.search(r'\b\d+\b', length).group()
                
    return rt_films_data

