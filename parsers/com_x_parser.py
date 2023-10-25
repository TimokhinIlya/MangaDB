from utils import webdriver, Service, BeautifulSoup, re, sleep

# Функция для получения главы манги
def get_manga_chapter(manga_name: str) -> tuple:

    # Настройка веб-драйвера
    service = Service(executable_path="parsers\\chromedriver\\chromedriver.exe")
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)

    # Формирование URL для поиска манги
    url = f'https://com-x.life/index.php?do=search&subaction=search&search_start=0&full_search=0&story={manga_name}'

    try:
        # Получение страницы манги
        driver.get(url)

        # Задержка
        sleep(0.1)

        # Получение HTML-кода страницы
        html = driver.page_source
        
        # Инициализация парсера BeautifulSoup
        soup = BeautifulSoup(html, 'lxml')

        # Поиск тега ссылки на мангу
        href_tag = soup.find('a', class_ = 'readed__img img-fit-cover anim')

        # Получение URL манги
        if href_tag:
            href_value = href_tag.get('href')

        manga_url = href_value

        # Формирование URL страницы с главами манги
        manga_chapters = f'{manga_url}#chapters'

        driver.get(manga_chapters)

        sleep(0.1)

        # Получение HTML-кода страницы с главами манги
        html = driver.page_source
        
        # Инициализация парсера BeautifulSoup для страницы с главами манги
        soup = BeautifulSoup(html, 'lxml')

        # Поиск тега с информацией о последней главе
        title_tag = soup.find('div', class_='cl__item d-flex ai-center jc-space-between')

        last_chapter = None

        # Проверка наличия тега с информацией о последней главе
        if title_tag:
            # Получение информации о последней главе
            title = title_tag.get('title')
            # Извлечение номера последней главы
            last_chapter = max(re.findall(r'\d+', title))

        # Получение даты последней главы
        chapter_date = soup.find('div', class_='cl__item-date').get_text().strip()
        
        # Возвращение URL манги, номера последней главы и даты последней главы
        return manga_url, float(last_chapter), chapter_date

    # Обработка исключений
    except Exception as e:
        print(f'Ошибка: {e}')
        return None
    
    # Завершение работы веб-драйвера
    finally:
        driver.close()
        driver.quit()

def com_x_parser(manga_name: str) -> tuple:

    # Устанавливаем множество имен манги для парсинга
    manga_set = {'Берсерк', 'Синяя Тюрьма: Блю Лок', 'Магическая битва'}

    if manga_name in manga_set:
        return get_manga_chapter(manga_name)
    else:
        return None
