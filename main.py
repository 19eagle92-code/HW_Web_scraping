import requests
import re
from bs4 import BeautifulSoup
from full_article import full_article_by_keywords

URL = "https://habr.com/ru/articles/"
BASE_URL = "https://habr.com"
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}

response = requests.get(URL, headers=HEADERS)
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
        link = BASE_URL + link

    # Ищем дату
    date_tag = article.find("time")
    date = date_tag["datetime"][:10] if date_tag else "Без даты"

    # Видимый текст статьи
    preview_text = article.get_text().lower()

    # Проверяем ключевые слова по заголовку
    if any(keyword.lower() in preview_text for keyword in KEYWORDS):
        print(f"{date} – {title} – {link}")
    # Проверяем ключевые слова по тексту статьи
    elif full_article_by_keywords(link, HEADERS, KEYWORDS):
        print(f"{date} – {title} – {link}")
