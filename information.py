import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image, ImageFilter, ImageEnhance

#영화 제목 데이터프레임, 영화 별점 데이터프레임, 그리고 그걸 합친 데이터프레임.
movie_id_titles_df = pd.read_csv('./data/Movie_Id_Titles')

movie_ratings_df = pd.read_csv('./data/u.data', sep = '\t', names = ['user_id', 'item_id', 'rating', 'timestamp'])
movie_df = pd.merge(movie_id_titles_df,movie_ratings_df, on = 'item_id')


#영화별 리뷰 갯수
movie_review_count = movie_df['title'].value_counts()

#영화별 별점 평균
movie_rating = movie_df.groupby('title')['rating'].mean()

#영화별 리뷰 + 별점
movie_review_count_rating =pd.concat([movie_review_count,movie_rating], axis = 1)

#영화별 리뷰 + 별점인데 인덱스를 초기화했음
movie_review_count_rating.reset_index(inplace = True)
movie_review_count_rating.columns = ['title', 'review_counts', 'average_rating']

#영화별 리뷰 + 별점 데이터프레임을 컬럼명을 알아보기 쉽게 바꿔줌
# movie_review_count_rating.columns = ['영화 제목','리뷰 수', '평균 별점']



def run_information():
    st.title("영화")
    st.write('\"영화(映畵, 영어: film)는 순간을 기록한 장면을 연속적으로 촬영하여 기록한 동영상을, 같이 기록한 음성과 함께 편집하여 어떤 내용을 전달하게끔 꾸며서 만든 영상물입니다.\"',)
    st.write('20세기 후반에 들어서면서 영화 산업은 단순한 예술의 한 장르가 아닌, 거대한 엔터테인먼트 산업으로 변화하였고, 2010년 기준으로 전 세계의 극장매출은 300억달러를 돌파하며 현재 2017년에는 그보다 한참 높아진 시장크기를 지니게 되었습니다.')

    col1, col2 = st.beta_columns([2,6])  #1:4의 비율로 컬럼 두개의 영역을 잡아달라.

    with col1 :
        st.image('data/titanic_poster.jpg')

    with col2 :
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('''영화 흥행성적은 타이타닉의 압도적인 매출에 국한되어 있었지만,
        아바타로 제임스 카메론이 스스로의 기록을 갱신하고부터
        헐리우드의 흥행성적 경쟁에 불이붙어 현재는 전세계 흥행성적이 10억불이 넘어가는 영화가 30개 정도를 돌파하여
        스타워즈나 어벤져스 같은 신세대 헐리우드 블록버스터들이 차지하고 있습니다.''')
