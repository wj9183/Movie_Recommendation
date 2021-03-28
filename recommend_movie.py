import pandas as pd
import streamlit as st

movie_id_titles_df = pd.read_csv('Movie_Id_Titles')
movie_ratings_df = pd.read_csv('u.data', sep = '\t', names = ['user_id', 'item_id', 'rating', 'timestamp'])
movie_df = pd.merge(movie_id_titles_df,movie_ratings_df, on = 'item_id')

movie_review_count = movie_df['title'].value_counts()

movie_review_count

movie_rating = movie_df.groupby('title')['rating'].mean()

movie_rating

movie_review_count_rating =pd.concat([movie_review_count,movie_rating], axis = 1)

movie_review_count_rating.reset_index(inplace = True)

movie_review_count_rating.columns = ['영화 제목','리뷰 수', '별점']

movie_matrix = movie_df.pivot_table(values = 'rating', index = 'user_id', columns = 'title')




def recommend_movie():

    menu = ['','취향에 맞는 영화로부터 추천받기', '취향에 맞지 않은 영화로부터 추천받기']
    select_menu = st.selectbox('추천받을 방법을 고르세요', menu)
    if select_menu == '취향에 맞는 영화로부터 추천받기':
        favorite_movie = st.text_input('취향이였던 영화 제목을 입력하세요')
        



    










    st.write('30개 이하의 리뷰를 받은 영화들은 추천되지 않습니다.')


