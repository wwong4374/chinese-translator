import logging
import requests
from bs4 import BeautifulSoup

logging.getLogger().setLevel(logging.INFO)

def get_article_title(url: str) -> str:
    # #main > div:nth-child(1) > h1
    # print(f"MAIN: {main}")  # TODO: remove
    ...

def get_article_content(url: str) -> str:
    ... 

# url = input("Please provide link to WSJ article: ")
url = "https://archive.ph/aKbY9"  # TODO: remove

logging.info(f"Parsing article at: {url}")  
html = requests.get(url=url).text
soup = BeautifulSoup(html, "html.parser")

logging.info(f"Parsed HTML: {soup.prettify()}")  # TODO: remove
main = soup.find("main", {"id": "main"}).findChild("div")
# print(f"MAIN: {main}")  # TODO: remove

