from utils import requests, BeautifulSoup, json, re

def get_manga_link(manga_name: str) -> str:
    try:
        # Получение JSON-данных из ссылки
        json_url = f'https://api.remanga.org/api/search/?query={manga_name}&count=5&field=titles'

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }

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
        
    except Exception as e:
        print(f"Error on remanga_parser - {manga_name}: {e}")
        return None

def get_manga_id(manga_url: str) -> str:
    try:
        # Проверка, не является ли manga_url пустой
        if manga_url is not None:

            # Запрос к URL страницы с мангой
            response = requests.get(manga_url)

            # Парсинг HTML-страницы с помощью BeautifulSoup
            soup = BeautifulSoup(response.text, "lxml")

            # Поиск тега 'script', содержащего информацию о манге
            script_tag = soup.find("script", string=lambda x: "branches" in str(x))

            # Извлечение JSON-данных из текста скрипта
            json_data = re.search(r'({.*})', str(script_tag)).group(0)

            # Преобразование JSON-данных в словарь
            data_dict = json.loads(json_data)

            # Извлечение значения id манги из данных
            manga_id = data_dict['props']['pageProps']['fallbackData']['content']['branches'][0]['id']

            return manga_id
        else:
            return None
        
    except Exception as e:
        print(f"Error on remanga_parser - {manga_url}: {e}")
        return None
    
def get_manga_chapter(manga_id: int) -> tuple:
    try:
        # Проверка, не является ли manga_id пустой
        if manga_id is not None:

            # Формирование URL для получения JSON-данных о главах манги
            json_url = f'https://api.remanga.org/api/titles/chapters/?branch_id={manga_id}&ordering=-index&user_data=1&count=40&page=1'

            # Получение JSON-данных из URL
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
        
    except Exception as e:
        print(f"Error on remanga_parser - {manga_id}: {e}")
        return None
    
def remanga_parser(manga_name:str)-> tuple:
    # Устанавливаем исключения
    manga_set = {'Кэнган Омега'}

    if manga_name not in manga_set:
        manga_tuple = tuple()
        manga_url = get_manga_link(manga_name)
        manga_id = get_manga_id(manga_url)
        manga_chapter = get_manga_chapter(manga_id)

        if manga_url and manga_id and manga_chapter is not None:
            manga_tuple = (manga_url,) + manga_chapter
            return manga_tuple