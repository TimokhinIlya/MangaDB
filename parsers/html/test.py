import re
import json
from bs4 import BeautifulSoup

with open("parsers\html\manga_page.html", "r", encoding="utf-8") as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, "lxml")

script_tag = soup.find("script", string=lambda x: "branches" in str(x))

json_data = re.search(r'({.*})', str(script_tag)).group(0)

data_dict = json.loads(json_data)

# Извлечение branches id
branches_id = data_dict['props']['pageProps']['fallbackData']['content']['branches'][0]['id']

print(branches_id)



