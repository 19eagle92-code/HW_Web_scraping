import requests
import re

URL = "https://habr.com/ru/articles/"

response = requests.get(URL)
# print(response.request.headers)

# Определяем список ключевых слов:
KEYWORDS = ["дизайн", "фото", "web", "python"]

markup = response.text
# print(markup)

matches = re.findall(r"дизайн", markup)
print(matches)


# for word in KEYWORDS:
#     matches = re.findall(word, markup)
#     print(f" для слова '{word}' найдено - {len(matches)} совпадений")
