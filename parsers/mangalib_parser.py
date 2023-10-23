import requests
from bs4 import BeautifulSoup
import json
import re

def get_manga_chapter(manga_name: str) -> tuple:

    json_url = f"https://mangalib.me/search?type=manga&q={manga_name}"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(json_url, headers=headers)
    data = response.json()

    for content in data:
        if content['rus_name'].lower() == manga_name.lower():
            manga_url = content['href']
            break

    response = requests.get(manga_url, headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')
    # Находим тег <script> в HTML
    script_tag = soup.find('script')

    # Извлекаем текст скрипта
    script_text = script_tag.string

    pattern = re.compile(r'window\.__DATA__\s*=\s*({.*?});', re.DOTALL)
    match = pattern.search(script_text)
    if match:
        data_text = match.group(1)
        data = json.loads(data_text)
    else:
        print("JSON data not found.")

    # Получаем первый элемент списка "list" внутри "chapters"
    chapters = data['chapters']['list'][0]

    # Извлекаем значение "chapter_number" из первого элемента
    last_chapter = chapters['chapter_number']
    chapter_date = chapters['chapter_created_at']

    return manga_url, float(last_chapter), chapter_date

def mangalib_parser (manga_name:str)-> tuple:
    try:
        return get_manga_chapter(manga_name)
    except Exception as e:
        return f"Произошла ошибка при обработке запроса: {e}"