import requests
from bs4 import BeautifulSoup

rating_pages = []

response = requests.get("https://workey.codeit.kr/ratings/index")
rating_page = response.text

soup = BeautifulSoup(rating_page, 'html.parser')

program_title_tags = soup.select('td.program')

td_tags = soup.select('td')[:4]

for tag in td_tags:
    print(tag.get_text())
