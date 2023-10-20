import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

def get_manga_chapter(manga_name: str) -> tuple:

    json_url = f"https://readmanga.live/search/suggestion?query={manga_name}&types[]=CREATION&types[]=FEDERATION_MANGA_SUBJECT"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    # Преобразование URL-адреса с использованием urllib.parse.quote()
    encoded_url = quote(json_url, safe=':/?&=')

    response = requests.get(encoded_url, headers=headers)
    data = response.json()

    link = None

    for suggestion in (data['suggestions']):
        if suggestion['value'] == manga_name:
            link = suggestion['link']
            break

    if link is not None:
        manga_url = f"https://readmanga.live/{link}"
    else:
        manga_url = None

    response = requests.get(manga_url, headers=headers)

    soup = BeautifulSoup(response.text, "lxml")

    number = soup.find('a', class_='chapter-link read-last-chapter')

    date = soup.find('td', class_='d-none d-sm-table-cell date text-right')

    if number:
        href_value = number.get('href')  # Получаем значение атрибута href
        last_chapter = href_value.rsplit('/', 1)[-1]

    if date:
        chapter_date = date.get_text(strip=True)

    return manga_url, float(last_chapter), chapter_date

def readmanga_parser (manga_name:str)-> tuple:
    try:
        return get_manga_chapter(manga_name)
    except Exception as e:
        return f"Произошла ошибка при обработке запроса: {e}"

