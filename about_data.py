import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sb


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

movie_rating = movie_rating.reset_index()
movie_rating.columns = ['title','rating']
st.dataframe(movie_rating)


def run_about_data():

    menu = ['보고 싶은 통계를 골라주세요.', '가장 많은 리뷰가 달린 영화들', '가장 평점이 높은 영화들', '평점과 평점에 대한 신뢰도가 가장 높은 영화들']
    select_menu = st.selectbox('보고 싶은 통계를 골라주세요.', menu)
    if select_menu == '가장 많은 리뷰가 달린 영화들':
        select_amount = st.slider('상위 몇 개의 영화에 대한 차트를 보고 싶은지 고르세요.', 0, 20)
        if select_amount != 0:
            most_reviewed_chart_data1 = movie_df['title'].value_counts().head(select_amount)
            fig = plt.figure()
            plt.barh(most_reviewed_chart_data1.index, most_reviewed_chart_data1)  #x축 y축.   #연도별 배당금을 알 수 있다.
            plt.title('The Most Reviewed Movies')
            plt.ylabel('Movie Title')
            plt.xlabel('Reviews')
            st.pyplot(fig)

    if select_menu == '가장 평점이 높은 영화들':
        select_amount = st.slider('상위 몇 개의 영화에 대한 차트를 보고 싶은지 고르세요.', 0, 20)
        if select_amount != 0:
            fig = plt.figure()
            highest_rated_chart_data = movie_rating.sort_values('rating', ascending = False).head(select_amount)

            plt.barh(highest_rated_chart_data['title'], highest_rated_chart_data['rating'])  #x축 y축.   #연도별 배당금을 알 수 있다.
            plt.title('The Highest Rated Movies')
            plt.ylabel('Movie Title')
            plt.xlabel('Reviews')
            st.pyplot(fig)


    if select_menu == '평점과 평점에 대한 신뢰도가 가장 높은 영화들':
        select_amount = st.slider('상위 몇 개의 영화에 대한 차트를 보고 싶은지 고르세요.', 0, 20)
        if select_amount != 0:
            # movie_review_count_rating.columns = ['title', 'review_counts', 'average_rating']

            movie_review_count_rating['total_rating'] = movie_review_count_rating['review_counts'] * movie_review_count_rating['average_rating']

            top_rated_movie = movie_review_count_rating['total_rating'].max()

            movie_review_count_rating['total_rating'] = movie_review_count_rating['total_rating'] / top_rated_movie * 100
            total_rating_chart_data = movie_review_count_rating.sort_values('total_rating', ascending = False).head(select_amount)

            fig = plt.figure()
            plt.barh(total_rating_chart_data['title'], total_rating_chart_data['total_rating'])  #x축 y축.   #연도별 배당금을 알 수 있다.
            plt.title('The Highest Rated Movies')
            plt.ylabel('Movie Title')
            plt.xlabel('Total Score')
            st.pyplot(fig)


    pass

