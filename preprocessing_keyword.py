import csv
from tqdm import trange
from collections import Counter
from konlpy import jvm
from konlpy.tag import Okt
from konlpy.tag import Twitter
import numpy as np
import pandas as pd
from pandas import DataFrame

#jvm.init_jvm()
okt = Okt()
df = pd.read_csv("18년도 취업.csv", names = ['title', 'content'],encoding='cp949')

text = df['title']

top20_nouns=[]
temp_total = (i for i in text)
for i in trange(len(text)):
    t_t = next(temp_total)
    c = Counter(okt.nouns(t_t))   
    top20_nouns.append([word for word,cnt in c.most_common(20)])


# record 별로 뽑힌 20개의 최빈명사들을 nouns에 합치기
nouns = []
for word_chunk in top20_nouns :
    for word in word_chunk :
        nouns.append(word)
nouns.sort() # ㄱ-ㅎ 정렬


unique_nouns = list(set(nouns)) # 명사 별로 한개씩만 남김(명사 별 개수 세기 위함)
unique_nouns.sort() # 정렬

noun_count = [] # 명사 별 개수 들어감
for noun in unique_nouns :
    count = 0
    for word in nouns :
        if count != 0 and word != noun :
            break;
        if word == noun : 
            count = count + 1
    noun_count.append(count)

# Data Frame 으로 만들기
nouns_df = pd.DataFrame()
nouns_df.loc[:, 'NOUN'] = unique_nouns
nouns_df.loc[:, 'COUNT'] = noun_count

# csv 파일로 별도 저장
nouns_df.to_csv('NOUNS.csv')

'''
TDM = dummy.T
word_counter = TDM.sum(axis =1)
print(word_counter)


# 빈도수 시각화하기
word_counter.plot(kind='barh',title='specup word counter')

# 내림차순 정렬
word_counter.sort_values().plot(kind='barh',title='specup word counter')
plt.show()

'''




