import requests
from bs4 import BeautifulSoup
import re
import json

def get_manga_link(manga_name: str) -> str: # Получаем ссылку на страницу с искомой мангой

    json_url = f'https://api.remanga.org/api/search/?query={manga_name}&count=5&field=titles'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    # Получение JSON-данных из ссылки
    response = requests.get(json_url, headers=headers)
    data = response.json()

    eng_name = None

    for content in (data['content']):
        if content['main_name'].lower() == manga_name.lower():
            eng_name = content['dir']
            break
    if eng_name is not None:
        manga_url = f"https://remanga.org/manga/{eng_name.replace(' ','-')}"
        return manga_url
    else:
        return None


def get_manga_id(manga_url:str) -> str: # Получаем id манги

    if manga_url is not None:
        # URL страницы с мангой
        response = requests.get(manga_url)

        # Разбор HTML-страницы с помощью Beautiful Soup
        soup = BeautifulSoup(response.text, "lxml")

        script_tag = soup.find("script", string=lambda x: "branches" in str(x))

        json_data = re.search(r'({.*})', str(script_tag)).group(0)

        data_dict = json.loads(json_data)

        manga_id = data_dict['props']['pageProps']['fallbackData']['content']['branches'][0]['id']

        return manga_id
    else:
        return None

def get_manga_chapter(manga_id:int)-> tuple: # Получаем последную главу манги
    if manga_id is not None:
        json_url = f'https://api.remanga.org/api/titles/chapters/?branch_id={manga_id}&ordering=-index&user_data=1&count=40&page=1'
        # Получение JSON-данных из ссылки
        response = requests.get(json_url)
        data = response.json()

        last_chapter, chapter_date = None, None

        for content in (data['content']):
            if not content['is_paid']:
                last_chapter, chapter_date = content['chapter'], content['upload_date']
                break

        return float(last_chapter), chapter_date
    else:
        return None

def remanga_parser (manga_name:str)-> tuple:
    try:
        manga_tuple = tuple()
        manga_url = get_manga_link(manga_name)
        if manga_url is not None:
            manga_id = get_manga_id(manga_url)
            manga_tuple = (manga_url,) + get_manga_chapter(manga_id)
            return manga_tuple
        else:
            return None
    except Exception as e:
        return f"Произошла ошибка при обработке запроса: {e}"