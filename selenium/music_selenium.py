# 라이브러리 임포트
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# 크롬 드라이버 생성
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 3)


# 사이트 접속하기
driver.get('https://workey.codeit.kr/music')
sleep(1)


popular_artist = []

for element in driver.find_elements(by=By.CSS_SELECTOR, value='ul.popular__order li'):
    popular_artist.append(element.text.strip())

print(popular_artist)


# 5초 기다리기
sleep(5)


# 크롬 드라이버 종료
driver.quit()
