import requests
from bs4 import BeautifulSoup

# URL страницы с информацией о манге
url = "https://remanga.org/manga/omniscient-reader"

# Отправка GET-запроса и получение HTML-страницы
response = requests.get(url)

# Проверка успешности запроса
if response.status_code == 200:
    # Разбор HTML-страницы с помощью Beautiful Soup
    soup = BeautifulSoup(response.text, "html.parser")

    # Извлечение заголовка манги
    manga_title = soup.find("h1").text.strip()

    print(f"Заголовок манги: {manga_title}")

else:
    print("Ошибка при запросе страницы")