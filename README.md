# Capstone-design 1
## 1. 레파지토리(repository) 소개
  본 레파지토리(repository)는 2020-1학기 캡스톤 디자인1의 활동을 담았다.
  repository의 내용은 텍스트마이닝을 위하여 공부한 TextMining with R 코드(text ming with R 01~06.R)와 프로젝트에 사용한 구현코드로 이루어져 있다. 
  * text ming with R 01~06.R의 경우, Julia silge & David Robinson의 'TextMining with R: A tidy approach'를 참고하여 실습하였다. 
  
## 2. 프로젝트 소개
  프로젝트는 "텍스트 마이닝을 위한 취업관련 커뮤니티 분석"이란 주제로 진행되었다. 본 프로젝트에서는 취업 관련 커뮤니티를 대상으로 텍스트 마이닝을 이용하여 취업 시장의 실태, 커뮤니티 사용자들의 실제적 고민 및 니즈, 커뮤니티 별 특징을 파악하는 것을 목적으로 삼고 있다.

### 2-1. 데이터 수집 (data collection_crawling)
취업관련 커뮤니티 카페 2곳 (이 문서에서는 임의로 A, B 카페로 별칭하였다.) 의 ‘취업’ 키워드가 들어간 15~19년도 게시글을 데이터 수집대상으로 선정하였다. 

데이터 수집 방식은 웹크롤링(Web Crawling)으로 다음과 같은 패키지(Package)를 사용하여 진행하였다.

1.  beautiful soup : html코드를 python가 이해하는 객체구조로 변환해주는 parsing역할
2.  selenium : 웹페이지 내의 특정요소들을 찾아내는 역할

웹크롤링 최종 결과 **A카페 25,586개, B카페 221,140개**의 데이터를 수집할 수 있었다.

### 2-2. 데이터 전처리 (preprocwssing_keyword)
데이터 전처리는 Python의 KoNLPy를 사용하여 진행하였다. KoNLPy의 5개의 형태소 분석기 중 Okt를 사용하여 크롤링된 데이터(제목/게시물/작성시각)를 한 달을 기준으로, 명사와 형용사의 빈도를 추출하였다.

### 2-3. 데이터 분석 및 시각화 (wordcloud_color image)
데이터분석은 연도별 최빈 단어 상위 10개를 추출, 단어드의 가중치를 계산하여 5년간 단어들의 빈도추이를 파악하는 방식으로 진행하였다. 

또한, 워드클라우드와 꺾은선 그래프를 통해 각 카페에서 5년간 언급된 단어들을 시각화하였다. 위드클라우드의 단어는 빈도가 클수록 글자크기가 크게 표현됨으로 커뮤니티 사용자가 어떤 주제에 관심을 갖고 있는지를 한번에 파악하기 용이하다. 꺾은선 그래프의 경우, 시간의 흐름대로 최빈 단어 상위 10의 증감소 추이를 각기 다른 선으로 나타내어 한번에 취업 트렌드의 변화를 파악하기에 효과적이다.
