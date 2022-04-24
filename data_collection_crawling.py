from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup as bs
import pandas as pd
import csv
import time
import requests
import chardet

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.implicitly_wait(3)
"""
# Create csv file
total_list = ['말머리', '제목', '내용'] 
f = open('파일이름', 'w', encoding = 'utf-8', newline='') 
wr = csv.writer(f)
wr.writerow([total_list[0], total_list[1], total_list[2]])
f.close()
 """
# Login Page
print("네이버 로그인")
####네이버 로그인###
# https://sab-jil.tistory.com/2
driver.get('https://nid.naver.com/nidlogin.login')

id = '네이버 아이디'
pw = '네이버 비밀번호'

driver.execute_script("document.getElementsByName('id')[0].value=\'" + id + "\'")
time.sleep(1)
driver.execute_script("document.getElementsByName('pw')[0].value=\'" + pw + "\'")
time.sleep(1)
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()  # 엔터 없이 바로 연결

# cafe main page url
cafe_url = "카페주소"  
driver.get(cafe_url)
time.sleep(3)

# 까페 목록 출력 페이지 지정, 옵션 설정

pages = 1 # 여기에 max page 쓰기
count = 0
scafe = []
stitle = []  # 게시글 제목
scontent = []  # 게시글 내용
dates = []
content_tags = []
board_url ="카페 검색창 주소(.page=)"
driver.get(board_url)
time.sleep(1) 
driver.switch_to.frame("cafe_main")

for i in range(1, pages + 1):
    count = i
    # urls=[]
    url = board_url + str(i)
    driver.get(url)
    time.sleep(1)

    iframe = driver.find_element_by_id('cafe_main')
    driver.switch_to.frame(iframe)

    # Selenium 제목 링크추출
    ###중요### 카페 소스페이지 태그가 변경되었습니다. 링크는 아래수정
    # links = driver.find_elements_by_css_selector('span.aaa a.m-tcol-c')
    links = driver.find_elements_by_css_selector('div.board-list a.article')
    urls = [i.get_attribute('href') for i in links]

    ####게시글목록 네이버ID, 닉네임정보 ...
    ##정규식 단어추출 "article_naverID_"
    ### nid for 추출
    # npattern = 'article_[a-zA-Z0-9]+'

    print("게시글 크롤링 시작 Page = ", count)

    # Beautifulsoup 활용 제목, 내용 크롤링
    for conurl in urls:  # 아래 두번째 들여쓰기
        try:
            try:  # 게시글이 삭제되었을 경우가 있기 때문에 try-exception
                driver.get(conurl)
                time.sleep(1)
                # content 글내용도 switch_to_frame이 필수
                driver.switch_to.frame('cafe_main')
                soup = bs(driver.page_source, 'html.parser')
                try:  
                    title = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.CLASS_NAME, "title_text"))
                    )
                    #print(title.text)
                    stitle.append(title.text)

                    date = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.CLASS_NAME, "date"))
                    )
                    #print(date.text)
                    dates.append(date.text)


                    #contentrenderer
                    content_tags = soup.select('div.ContentRenderer')[0].select('p')
                    
                    content = ' '.join([tags.get_text() for tags in content_tags])
                    scontent.append(content)
                   

                except TimeoutException:
                    print("해당 페이지에 app을 가진 ID를 가진 태그가 존재하지 않거나, 해당 페이지가 10초 안에 열리지 않았습니다.")

                # 여기 인거 같은데~~~~!!!!

                # cframe = driver.find_element_by_id('cafe_main')
                # driver.switch_to_frame(cframe)
                # contentSource = driver.page_source
                # soup = bs(contentSource, 'html.parser')

                # 제목 검색
                # [수정]2018.5.9 css tag 빈공간 에러발생
                # "span[class='b m-tcol-c']" → 'div.fl span.b'
           
                print([pages, count, len(stitle)])  # page로는 진행상황, cnt로는 몇개의 데이터


            except:  # chrome alert창 처리해줌
                driver.switch_to_alert.accpet()
                driver.switch_to_alert
                driver.switch_to_alert.accpet()
        except:
            pass
  
    time.sleep(1)

    print("title lengh=", len(stitle))

    ### DataFrame 으로 변환하기위한 리스트저장 ###
    # 게시글 제목,닉네임,네이버ID,링크,내용
    ##[수정] 2018.5.8
    # for 문 사용대신 DataFrame에서 전치행렬로 변환가능
    # tranposed matrix 명령어
    # scafe = pd.DataFrame([stitle, snickname, surl, scontent, naverIDs])
    # scafe = scafe.T
    ##[수정.끝]...
# 첫번째 for 문 끝
print("제목 내용 날짜 크롤링 완료")

scafe = pd.DataFrame([stitle, scontent, dates])
scafe = scafe.T
scafe = pd.DataFrame(scafe)
scafe.to_csv('저장할 파일명.csv',encoding='utf-8-sig', index=True)

# PhantomJS Browser Close
driver.close()
