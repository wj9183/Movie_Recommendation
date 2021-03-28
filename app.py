import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from find_movie import run_find_movie
from recommend_movie import recommend_movie


def main():


    menu = ['취미로서의 영화', '영화 직접 찾기', '영화 추천 프로그램', '수집되어있는 데이터 수집 현황']
    select_menu = st.sidebar.selectbox('Menu', menu)


    if select_menu == '취미로서의 영화':
        st.write('취미로서 영화가 어떤지 알려줌')
    elif select_menu == '영화 직접 찾기':
        run_find_movie()
    elif select_menu == '영화 추천 프로그램':
        recommend_movie()
    elif select_menu == '수집되어있는 데이터 수집 현황':
        pass
    else:
        st.write('잘못된 접근입니다.')
        pass


if __name__ == '__main__':
    main()