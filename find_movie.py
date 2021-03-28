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





def run_find_movie():

    menu = ['', '영화 제목으로 검색', '카테고리 별로 보기']
    movie_id_titles_df = pd.read_csv('Movie_Id_Titles')
    select_menu = st.selectbox('무엇을 기준으로 영화를 찾으시겠습니까?', menu)
    if select_menu == '영화 제목으로 검색':
        search_title()
    elif select_menu == '카테고리 별로 보기':
        search_category()
        pass
    else:
        pass


def search_title():
    searched_title = st.text_input('영화 제목을 입력하세요')
    if len(searched_title) != 0:
        st.dataframe(movie_id_titles_df.loc[movie_id_titles_df['title'].str.lower().str.contains(searched_title.lower()) == True,]['title'])
    else:
        pass



def search_category():
    menu = ['리뷰 수', '별점']
    select_category = st.selectbox('카테고리를 고르세요.', menu)   #멀티셀렉트 박스로 바꾸기. + 표 사이즈 계속 바뀌지 않는 게 뭐가 있었는데.
    st.dataframe(movie_review_count_rating.loc[:, ['영화 제목' , select_category]])    

    
