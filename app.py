import requests

def get_article_text(url: str) -> str:
    # #wsj-article-wrap > div.article-content
    ...

url = input("Enter a url: ")
page = requests.get(url)
print (f"RESPONSE: {page}")
contents = page.contents
print(f"PAGE CONTENTS: {contents}")