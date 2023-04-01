# Scraping script

Script that get articles from the site and send them to the telegram channel.
Every 15 seconds script check new articles on the site. And if there is new articles,
it sends them to the channel.

Libraries used: 
- bs4
- python-dotenv
- python-telegram-bot
- httpx

Steps for using:
1. git clone
2. python -m venv venv
3. source : - venv/bin/activate
4. pip install -r requirements.txt
5. To set environment variables
6. python parse.py
