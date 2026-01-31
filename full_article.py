import requests
from bs4 import BeautifulSoup


def full_article_by_keywords(url, headers, keywords):
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    article_body = soup.find("div", class_="tm-article-body")
    if not article_body:
        return False

    text = article_body.get_text().lower()
    return any(keyword.lower() in text for keyword in keywords)
