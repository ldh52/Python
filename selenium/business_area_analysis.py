import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # 드라이버 개체 정의
driver.get('https://sg.sbiz.or.kr/')  # 웹 페이지 로드
driver.maximize_window()  # 창 최대화

driver.implicitly_wait(20)

time.sleep(5)
try:
    for i in range(12,51):
        selector = f'#container > div:nth-child({i}) > div > div.head.close-option > div > label:nth-child(2)'
        try:
            element = driver.find_element(By.CSS_SELECTOR, selector)
            if element.text == '오늘 하루 이 창을 열지않음':
                element.click()
                break
        except:
            continue
except:
    pass

time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '#menu > div.lay.scrollbarView > div > div.head > div > ul > li > a > span').click()  # '로그인' 버튼 클릭

driver.find_element(By.CSS_SELECTOR, '#id').send_keys('***')  # 사용자 아이디
driver.find_element(By.CSS_SELECTOR, '#pass').send_keys('***')  # 사용자 비밀번호
driver.find_element(By.CSS_SELECTOR, 'body > div > div.l_content > form > div > input').click()  #'로그인' 버튼 누르기

time.sleep(5)
try:
    driver.find_element(By.CSS_SELECTOR, '#container > div:nth-child(12) > div > div.head.close-option > div > label:nth-child(2) > span').click()  # 오늘 하루 이 창을 열지 않음
except:
    pass

driver.find_element(By.CSS_SELECTOR, '#toLink > a > h4').click()  # '상세분석' 버튼 클릭

time.sleep(1)  # 검색 결과가 나올 때까지 조금 기다려 줌
driver.find_element(By.CSS_SELECTOR, '#adrsList > li:nth-child(1) > label > span').click()  # 검색 결과가 여러 개인 경우의 첫 번째 검색 결과 선택지
driver.find_element(By.CSS_SELECTOR, '#container > div:nth-child(1) > div:nth-child(3) > div.foot > a:nth-child(2)').click()  # 확인

driver.find_element(By.CSS_SELECTOR, '#upjong > ul > li:nth-child(2) > label').click()  # 음식
driver.find_element(By.CSS_SELECTOR, '#container > div:nth-child(17) > div > div.midd > div.midd > div.searchview.scrollbarView > div > ul > li.best > div > ul > li:nth-child(2) > label > span').click()  # 카페
time.sleep(0.5)  # 0.5초 쉬기
driver.find_element(By.CSS_SELECTOR, '#checkTypeConfirm > span').click()  # 확인

driver.find_element(By.CSS_SELECTOR, '#map > div:nth-child(1) > div > div:nth-child(6) > div:nth-child(2) > div > ul > li.child').click()  # 상권분석

driver.find_element(By.CSS_SELECTOR, '#map > div:nth-child(1) > div > div:nth-child(6) > div:nth-child(2) > div > ul > li.child > div > ul > li:nth-child(2) > label > svg').click()  # 반경
driver.find_element(By.CSS_SELECTOR, '#auto_circle > div > div.midd > ul > li:nth-child(3) > label').click()  # 300미터
driver.find_element(By.CSS_SELECTOR, '#auto_circle > div > div.foot > a:nth-child(2) > span').click()  # 확인

driver.find_element(By.CSS_SELECTOR, '#map > div:nth-child(1) > div > div:nth-child(6) > div:nth-child(3) > img').click()  # 분석

# 개선 코드
while True:
    driver.find_element(By.CSS_SELECTOR, '#printReport').click()
    try:
        driver.switch_to.alert.accept() # 알림창이 나타나면 '확인'을 누르고
        time.sleep(0.5)  # 0.5초를 더 쉼
    except:  # 만약 알림창이 나타나지 않아 '확인'을 누를 수 없는 경우
        break  # 보고서 생성이 완료되었다는 의미이므로 while 문 중단

driver.switch_to.window(driver.window_handles[1])  # 새로 열린 탭으로 포커스를 이동

driver.find_element(By.CSS_SELECTOR, '#OZViewer > div:nth-child(1) > input.oz_ui_layout.btnSAVEAS').click()  # 저장 버튼 클릭
driver.find_element(By.CSS_SELECTOR, 'body > div.ui-dialog.ui-corner-all.ui-widget.ui-widget-content.ui-front.ui-dialog-buttons.ui-draggable.oz_ui_layout > div.ui-dialog-buttonpane.ui-widget-content.ui-helper-clearfix > div > button:nth-child(2)').click()  # 확인 클릭

time.sleep(10)  # 보고서가 다운로드될 수 있도록 10초간 대기
driver.quit()  # 창 닫기
