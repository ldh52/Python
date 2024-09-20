import requests
from bs4 import BeautifulSoup

# HTML 코드 받아오기
response = requests.get("https://workey.codeit.kr/orangebottle/index")

# BeautifulSoup 타입으로 변환
soup = BeautifulSoup(response.text, 'html.parser')

# "phoneNum" 클래스를 가진 span 태그 선택하기
phone_number_tags = soup.select('span.phoneNum')

phone_numbers = []

# 텍스트 추출해서 리스트에 추가하기
for tag in phone_number_tags:
    phone_numbers.append(tag.get_text())

# 테스트 코드
print(phone_numbers)
