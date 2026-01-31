import requests
import re
from bs4 import BeautifulSoup

URL = "https://habr.com/ru/articles/"

response = requests.get(URL)
# print(response.request.headers)

# Определяем список ключевых слов:
KEYWORDS = ["дизайн", "фото", "web", "python"]

markup = response.text
# print(markup)

soup = BeautifulSoup(markup, "html.parser")
pretty_markup = soup.prettify()
# print(pretty_markup)

articles = soup.find_all("article")
# print(len(articles))

for article in articles:
    # Ищем заголовок
    title_tag = article.find("h2")
    # print(title_tag.text)
    if not title_tag:
        continue
    title = title_tag.text.strip()
    # print(title)

    # Ищем ссылку
    link = title_tag.find("a")["href"]
    if link.startswith("/"):
        link = "https://habr.com" + link
