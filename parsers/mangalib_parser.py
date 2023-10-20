import requests

def get_manga_chapter(manga_name: str) -> tuple:

    json_url = f"https://mangalib.me/search?type=manga&q={manga_name}"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(json_url, headers=headers)
    data = response.json()

    for content in data:
        if content['rus_name'] == manga_name:
            manga_url = content['href']
            last_chapter = content['chap_count']
            chapter_date = content['last_chapter_at']
            break

    return manga_url, float(last_chapter), chapter_date

def mangalib_parser (manga_name:str)-> tuple:
    try:
        return get_manga_chapter(manga_name)
    except Exception as e:
        return f"Произошла ошибка при обработке запроса: {e}"

