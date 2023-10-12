import requests
from bs4 import BeautifulSoup
from typing import Optional

def get_manga_link(manga_name: str) -> Optional[str]: # Функция получения ссылки на страницу с искомой мангой

    #   URL главной страницы
    url = "https://remanga.org/manga"

    # Отправка GET-запроса и получение HTML-страницы
    response = requests.get(url)

    try:
        response.raise_for_status() # Проверка наличия ошибок при запросе
        
        # Разбор HTML-страницы с помощью Beautiful Soup
        soup = BeautifulSoup(response.text, "lxml")


        # Извлечение заголовка манги
        element = soup.find('a', {'title': manga_name})

        if element:
        # Получите значение атрибута href
            href = element['href']
            # Получаем ссылку на страницу искомой манги
            manga_url = f'https://remanga.org{href}'
            return manga_url
        else:
            return f'Манга с названием "{manga_name}" не найдена'
    except requests.exceptions.RequestException as e:
        return f'Ошибка при отправке запроса: {e}'
    except Exception as e:
        return f'Произошла ошибка: {e}'
    
def get_manga_chapter(manga_url:str) -> Optional[str]: # Получаем ссылку из функции get_manga_link

    #   URL страницы с мангой
    response = requests.get(manga_url + '?p=content')
    
    response.raise_for_status() # Проверка наличия ошибок при запросе
    
    # Разбор HTML-страницы с помощью Beautiful Soup
    soup = BeautifulSoup(response.text, "lxml")

    # Извлечение последней вышедшей главы манги
    element = soup.find('p', {'class': 'Typography_body1__YTqxB Typography_color-inherit__Wstd_ Chapters_title__ocJer'})
    return element

print(get_manga_link('Легенда о северном клинке'))