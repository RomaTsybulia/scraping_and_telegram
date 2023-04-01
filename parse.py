import os
import time

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://www.tesmanian.com/"

token = os.getenv("TOKEN")
chat_id = os.getenv("CHAT_ID")


def parse_single_article(article_soup):
    title = article_soup.text.replace("&", "%26")
    link = BASE_URL + article_soup["href"]
    message = title + " " + link
    telegram_url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text="{message}"'
    requests.get(telegram_url)


def get_all_articles(last_article):
    page = requests.get(BASE_URL)
    soup = BeautifulSoup(page.content, "html.parser")

    articles_soup = soup.select(".blog-post-card__info > div > div > p > a")
    articles_soup.reverse()
    start_index = 0

    if last_article in articles_soup:
        start_index = articles_soup.index(last_article)
        articles_soup = articles_soup[start_index:]

    if start_index < len(articles_soup):
        for article_soup in articles_soup[start_index:]:
            parse_single_article(article_soup)

    return articles_soup[-1]


def main():
    last_article = ""
    while True:
        last_article = get_all_articles(last_article)
        time.sleep(15)


if __name__ == "__main__":
    main()
