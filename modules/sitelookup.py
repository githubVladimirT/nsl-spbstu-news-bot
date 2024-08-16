"""
Lookup for updates on NSL SPBSTU website
"""

import requests
from bs4 import BeautifulSoup

prev_new = {}


def month_prettify(month: str) -> str:
    months = {
        "Янв": "01",
        "Фев": "02",
        "Мар": "03",
        "Апр": "04",
        "Май": "05",
        "Июн": "06",
        "Июл": "07",
        "Авг": "08",
        "Сен": "09",
        "Окт": "10",
        "Ноя": "11",
        "Дек": "12",
    }

    return months[month]


def lookup_for_updates() -> (list, str):
    global prev_new

    headers = {
        "Accept": "text/html",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
    }

    req = requests.get("https://nsl.spbstu.ru/news/", headers)
    soup = BeautifulSoup(req.text, 'html.parser')
    last_news = []

    for new in soup.find_all('div', class_='news-item'):
        news = {
            "date": "",
            "title": "",
            "link": "",
        }

        tmp_day = new.find('div', class_='day').get_text()
        day = tmp_day if len(tmp_day) == 2 else "0" + tmp_day
        month = month_prettify(new.find('div', class_='month').get_text())
        year = soup.find('div', class_='year').get_text()

        title_raw = new.find('a', class_='title')
        title = title_raw.get_text()
        link = title_raw.get('href')

        news['date'] = f"{day}.{month}.{year}"
        news['title'] = title
        news['link'] = link

        last_news.append(news)

    if not prev_new:
        prev_new = last_news[-1]

    news = last_news[:last_news.index(prev_new):]

    if len(news) == 0:
        return [], "Обновлений нет"

    for i in news:
        if i['date'] == '' or i['title'] == '' or i['link'] == '':
            return {}, f"Возникла ошибка при получении данных\n```{i=}```"

    print(news)

    prev_news = news[0]

    return news.reverse(), ""
