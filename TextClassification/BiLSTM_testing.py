# https://wikidocs.net/94748
# BiLSTM 으로 한국어 스팀 리뷰 감성 분석하기
# 긍정적 리뷰 = 1; 부정적 리뷰 = 0

# 구글 콜랩에 미캡 설치하기 (Mecab)
# Colab에 Mecab 설치
# !git clone https://github.com/SOMJANG/Mecab-ko-for-Google-Colab.git
# %cd Mecab-ko-for-Google-Colab
# !bash install_mecab-ko_on_colab190912.sh

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import urllib.request
from collections import Counter
from konlpy.tag import Mecab
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

urllib.request.urlretrieve("https://raw.githubusercontent.com/bab2min/corpus/master/sentiment/steam.txt", filename="steam.txt")

total_data = pd.read_table('steam.txt', names=['label','reviews'])
print('전체 리뷰 개수 : ', len(total_data))

total_data['reviews'].nunique(), total_data['label'].nunique()
total_data.drop_duplicates(subset=['reviews'], inplace=True)
# reviews 열에서 중복인 내용이 있다면 중복 제거
print('총 샘플의 수 : ', len(total_data))
print(total_data.isnull().values.any())


# 2 -- 훈련데이터와 테스트 데이터 분리하기
train_data, test_data = train_test_split(total_data, test_size=0.25, random_state=42)
print('훈련용 리뷰의 개수 : ', len(train_data))
print('테스트용 리뷰의 개수 : ', len(test_data))

# 3 -- 레이블의 분포 확인
train_data['label'].value_counts().plot(kind = 'bar')
print(train_data.groupby('label').size().reset_index(name = 'count'))

# 4 -- 데이터 정제하기
# 한글과 공백을 재외하고 모두 제거
train_data['reviews'] = train_data['reviews'].str.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]","")
train_data['reviews'].replace('', np.nan, inplace=True)
print(train_data.isnull().sum())

test_data.drop_duplicates(subset = ['reviews'], inplace=True)  # 중복 제거
test_data['reviews'] = test_data['reviews'].str.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]","")  # 정규 표현식 수행
test_data['reviews'].replace('', np.nan, inplace=True)  # 공백은 null 값으로 변경
test_data = test_data.dropna(how='any')  # null 값 제거
print('전처리 후 테스트용 샘플의 개수 : ', len(test_data))

# 불용어 정의
stopwords = ['도', '는', '다', '의', '가', '이', '은', '한', '에', '하', '고', '을', '를', '인', '듯', '과',
             '와', '네', '들', '듯', '지', '임', '게', '만', '게임', '겜', '되', '음', '면']

