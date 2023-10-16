import requests

#'https://remanga.org/manga'
#'https://remanga.org/manga/legend-of-the-northern-blade?p=content'
#'https://remanga.org/search?query='

def url_gen(url:str):

    response = requests.get(url)

    with open("parsers\html\manga_page.html", "w", encoding="utf-8") as file:
        file.write(response.text)


