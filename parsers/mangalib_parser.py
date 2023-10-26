from utils import requests, BeautifulSoup, json, re

def get_manga_chapter(manga_name: str) -> tuple:
    try:
        # Формирование URL на основе названия манги
        url = f"https://mangalib.me/search?type=manga&q={manga_name}"

        # Настройка заголовков для имитации обычного браузера
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }

        # Запрос к URL и получение JSON-данных
        response = requests.get(url, headers=headers)
        data = response.json()

        manga_url = None

        # Поиск URL манги в полученных данных
        for item in data:
            if item['rus_name'].lower() == manga_name.lower():
                manga_url = item['href']
                break

        if manga_url == None:
            return None
        
        # Запрос к URL манги и получение HTML-страницы
        response = requests.get(manga_url, headers=headers)

        # Создание объекта BeautifulSoup для парсинга HTML
        soup = BeautifulSoup(response.text, 'lxml')

        # Находим тег <script> в HTML
        script_tag = soup.find('script')

        # Извлечение текста скрипта
        script_text = script_tag.string

        # Поиск нужных данных в тексте скрипта
        pattern = re.compile(r'window\.__DATA__\s*=\s*({.*?});', re.DOTALL)
        match = pattern.search(script_text)
        if match:
            data_text = match.group(1)
            data = json.loads(data_text)
        else:
            print("JSON data not found.")

        # Получение первого элемента списка "list" внутри "chapters"
        chapters = data['chapters']['list'][0]

        # Извлечение значений "chapter_number" и "chapter_created_at" из первого элемента
        last_chapter = chapters['chapter_number']
        chapter_date = chapters['chapter_created_at']

        return manga_url, float(last_chapter), chapter_date
    
    except Exception as e:
        print(f"Error on mangalib_parser - {manga_name}: {e}")
        return None
    
# Функция-обертка для получения данных о последней выпущенной главе манги
def mangalib_parser(manga_name: str) -> tuple:
    return get_manga_chapter(manga_name)