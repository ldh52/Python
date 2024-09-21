import requests
from bs4 import BeautifulSoup

response = requests.get("https://workey.codeit.kr/music")
music_page = response.text

soup = BeautifulSoup(music_page, 'html.parser')

# 인기 아티스트
popular_artist = []

# for tag in soup.select('ul.popular__order li'):
#     popular_artist.append(tag.get_text().strip())
#
# print(popular_artist)

for tag in soup.select('ul.popular__order li'):
    popular_artist.append(list(tag.stripped_strings)[1])

print(popular_artist)


# 검색어 순위
popular_searches = []

# <ul class="rank__order">에 중첩된 <li> 태그 선택
for tag in soup.select('ul.rank__order li'):

    # <li> 태그의 텍스트 요소 중 세 번째 가져오기
    search_word = list(tag.stripped_strings)[2]
    popular_searches.append(search_word)

# 출력 코드
print(popular_searches)
