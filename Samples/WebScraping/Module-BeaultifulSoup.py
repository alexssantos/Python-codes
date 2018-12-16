from bs4 import BeautifulSoup
import requests
# lxml é um modulo importado pelo BeautifulSoup e precisa estar instalado assim como qlq Modulo de Parse do BeautifulSoup

page = requests.get("http://pt.wikipedia.org/wiki/Brasil.html")
soup = BeautifulSoup(page, "lxml")
soup = BeautifulSoup(page.content, 'html.parser')


# Prettify - https://www.dataquest.io/blog/web-scraping-tutorial-python/
print(soup.prettify())