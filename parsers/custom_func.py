import requests
from bs4 import BeautifulSoup
from typing import Optional
import re
import json

def get_manga_link(manga_name: str) -> Optional[str]: # Функция получения ссылки на страницу с искомой мангой

    json_url = f'https://api.remanga.org/api/search/?query={manga_name}&count=5&field=titles'
    # Получение JSON-данных из ссылки
    response = requests.get(json_url)
    data = response.json()

    eng_name = None

    for content in (data['content']):
        if content['main_name'] == manga_name:
            eng_name = content['dir']
            break
    manga_url = f"https://remanga.org/manga/{eng_name.replace(' ','-')}"
    return manga_url
    
manga_url = get_manga_link('Наруто')
print(manga_url)

def get_manga_id(manga_url:str) -> Optional[str]: # Получаем id манги

    # URL страницы с мангой
    response = requests.get(manga_url)

    # Разбор HTML-страницы с помощью Beautiful Soup
    soup = BeautifulSoup(response.text, "lxml")

    script_tag = soup.find("script", string=lambda x: "branches" in str(x))

    json_data = re.search(r'({.*})', str(script_tag)).group(0)

    data_dict = json.loads(json_data)

    # Извлечение branches id
    branches_id = data_dict['props']['pageProps']['fallbackData']['content']['branches'][0]['id']

    return branches_id

manga_id = get_manga_id(manga_url)
print(manga_id)

def get_manga_chapter(manga_id)-> Optional[int]:
    
    json_url = f'https://api.remanga.org/api/titles/chapters/?branch_id={manga_id}&ordering=-index&user_data=1&count=40&page=1'
    # Получение JSON-данных из ссылки
    response = requests.get(json_url)
    data = response.json()

    last_chapter_with_null_price = None

    for content in (data['content']):
        if not content['is_paid']:
            last_chapter_with_null_price = content['chapter']
            break
    return last_chapter_with_null_price

print(get_manga_chapter(manga_id))