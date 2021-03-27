import pandas as pd
import streamlit as st



def run_find_movie(movie_id_titles_df):

    menu = ['', '영화 제목으로 검색', '카테고리 별로 보기']
    movie_id_titles_df = pd.read_csv('Movie_Id_Titles')
    select_menu = st.selectbox('무엇을 기준으로 영화를 찾으시겠습니까?', menu)
    if select_menu == '영화 제목으로 검색':
        search_title(movie_id_titles_df)
    elif select_menu == '카테고리 별로 보기':
        search_category(movie_id_titles_df)
        pass
    else:
        pass


def search_title(movie_id_titles_df):
    searched_title = st.text_input('영화 제목을 입력하세요')
    if len(searched_title) != 0:
        # st.write(searched_title) #임시
        #Star Wars (1977)
        st.dataframe(movie_id_titles_df.loc[movie_id_titles_df['title'].str.lower().str.contains(searched_title.lower()) == True,]['title'])
        #영화 이름에 대소문자가 섞여있고 숫자와 괄호와 띄어쓰기도 섞여있다. 전처리 후 비교해야한다. 포함하는 걸 찾을 거니까 숫자와 괄호는 필요없겠다.
        # #일단 영화 이름을 가져온다.
        # st.dataframe(movie_id_titles_df['title']

        # result = movie_id_titles_df.loc[movie_id_titles_df['title'].,]
        # st.dataframe(result)


def search_category(movie_id_titles_df)
    menu = ['평점']
    st.multiselectbox('카테고리를 고르세요.', menu)

    
