import pandas as pd
import streamlit as st

movie_id_titles_df = pd.read_csv('Movie_Id_Titles')


movie_ratings_df = pd.read_csv('u.data', sep = '\t', names = ['user_id', 'item_id', 'rating', 'timestamp'])
movie_df = pd.merge(movie_id_titles_df,movie_ratings_df, on = 'item_id')

movie_review_count = movie_df['title'].value_counts()

movie_rating = movie_df.groupby('title')['rating'].mean()

movie_review_count_rating =pd.concat([movie_review_count,movie_rating], axis = 1)

movie_review_count_rating.reset_index(inplace = True)

movie_review_count_rating.columns = ['영화 제목','리뷰 수', '별점']

movie_matrix = movie_df.pivot_table(values = 'rating', index = 'user_id', columns = 'title')




def recommend_movie():

    st.title('영화 추천 메뉴입니다.')

    menu = ['추천 받을 방법을 골라보세요.','취향에 맞는 영화로부터 추천받기', '취향에 맞지 않은 영화로부터 추천받기']
    select_menu = st.selectbox('추천받을 방법을 골라보세요', menu)

    if select_menu == '취향에 맞는 영화로부터 추천받기':
        user_typed_title = st.text_input('가장 취향에 맞았던 영화 제목을 입력하세요. (해당 영화가 등록된 전체 영화목록에 등록되어있어야 검색 가능합니다.)')

        # st.write(movie_id_titles_df.loc[movie_id_titles_df['title'].str.lower().str.contains(select_menu.lower()) == True,]['title'])
        favorite_movie = movie_id_titles_df.loc[movie_id_titles_df['title'].str.lower().str.contains(user_typed_title.lower()) == True, 'title']
        
        if favorite_movie != False:
            favorite_movie = favorite_movie.iloc[0]
        else:
            pass

        recommend_count = st.slider('몇 편의 영화를 추천받으시겠습니까?', 0, 50)
        least_review_counts = st.slider('최소 리뷰 갯수를 설정하세요. 리뷰가 너무 많거나 적으면 만족스러운 추천이 되지 못할 가능성이 있습니다.', 0,300)

        if (len(user_typed_title) != 0) and (favorite_movie != False) and (recommend_count != 0) and (least_review_counts != 0):

            st.success('영화 \"{}\"을 기준으로 추천된 영화 목록입니다.'.format(favorite_movie))

            similar_movies_list = pd.DataFrame()
            
            movie_correlations = movie_matrix.corr(min_periods=least_review_counts)

            similar_movie = movie_correlations[favorite_movie].dropna().sort_values(ascending = False).to_frame()
            similar_movie.columns = ['Correlation']
            similar_movie['Weight'] = similar_movie['Correlation'] * 5
            similar_movies_list = similar_movies_list.append(similar_movie)
            # st.dataframe(similar_movies_list.sort_values('Weight', ascending = False))
            st.dataframe(similar_movies_list.sort_values('Weight', ascending = False)[1:recommend_count + 1].index)
            st.warning('현재 {}개 이하의 리뷰를 받은 영화들은 추천되지 않고 있습니다.'.format(least_review_counts))



    elif select_menu == '취향에 맞지 않은 영화로부터 추천받기':

        user_typed_title = st.text_input('가장 취향에 맞지 않았던 영화 제목을 입력하세요. (해당 영화가 등록된 전체 영화목록에 등록되어있어야 검색 가능합니다.)')

        # st.write(movie_id_titles_df.loc[movie_id_titles_df['title'].str.lower().str.contains(select_menu.lower()) == True,]['title'])
        favorite_movie = movie_id_titles_df.loc[movie_id_titles_df['title'].str.lower().str.contains(user_typed_title.lower()) == True, 'title']
        favorite_movie = favorite_movie.iloc[0]

        if len(user_typed_title) != 0:

            similar_movies_list = pd.DataFrame()

            least_review_counts = st.slider('최소 리뷰 갯수를 설정하세요. 리뷰가 너무 많거나 적으면 만족스러운 추천이 되지 못할 가능성이 있습니다.', 1,300)

            st.success('영화 \"{}\"이 취향에 맞지 않았던 리뷰어들의 평가를 기준으로 추천된 영화 목록입니다.'.format(favorite_movie))
            
            movie_correlations = movie_matrix.corr(min_periods=least_review_counts)

            similar_movie = movie_correlations[favorite_movie].dropna().sort_values(ascending = False).to_frame()
            similar_movie.columns = ['Correlation']
            similar_movie['Weight'] = similar_movie['Correlation'] * 1
            similar_movies_list = similar_movies_list.append(similar_movie)
            # st.dataframe(similar_movies_list.sort_values('Weight', ascending = False))
            st.dataframe(similar_movies_list.sort_values('Weight', ascending = False)[1:recommend_count + 1].index)
            st.warning('현재 {}개 이하의 리뷰를 받은 영화들은 추천되지 않고 있습니다.'.format(least_review_counts))
        pass

    else:
        pass


    











