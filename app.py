import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from find_movie import run_find_movie


def main():


    movie_id_titles_df = pd.read_csv('Movie_Id_Titles')
    movie_ratings_df = pd.read_csv('u.data', sep = '\t', names = ['user_id', 'item_id', 'rating', 'timestamp'])
    movie_df = pd.merge(movie_id_titles_df,movie_ratings_df, on = 'item_id')
    menu = ['취미로서의 영화', '영화 직접 찾기', '영화 추천 프로그램', '수집되어있는 영화 전체 리스트']
    select_menu = st.sidebar.selectbox('Menu', menu)


    if select_menu == '취미로서의 영화':
        st.write('취미로서 영화가 어떤지 알려줌')
    elif select_menu == '영화 직접 찾기':
        run_find_movie(movie_id_titles_df)
    elif select_menu == '영화 추천 프로그램':
        pass
    elif select_menu == '수집되어있는 영화 전체 리스트':
        pass
    else:
        st.write('잘못된 접근입니다.')
        pass


if __name__ == '__main__':
    main()