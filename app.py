import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from find_movie import run_find_movie
from recommend_movie import recommend_movie
from information import run_information
from about_data import run_about_data


def main():


    menu = ['취미로서의 영화', '영화 직접 찾기', '영화 추천 프로그램', '수집되어있는 데이터 수집 현황']
    select_menu = st.sidebar.selectbox('Menu', menu)


    if select_menu == '취미로서의 영화':
        run_information()
    elif select_menu == '영화 직접 찾기':
        run_find_movie()
    elif select_menu == '영화 추천 프로그램':
        recommend_movie()
    elif select_menu == '수집되어있는 데이터 수집 현황':
        run_about_data()
    else:
        st.write('잘못된 접근입니다.')
        pass


if __name__ == '__main__':
    main()