import pandas as pd
import streamlit as st


#영화 제목 데이터프레임, 영화 별점 데이터프레임, 그리고 그걸 합친 데이터프레임.
movie_id_titles_df = pd.read_csv('Movie_Id_Titles')

movie_ratings_df = pd.read_csv('u.data', sep = '\t', names = ['user_id', 'item_id', 'rating', 'timestamp'])
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




#이 파일의 메인 함수
def run_find_movie():

    st.title('영화 검색 메뉴입니다.')
    menu = ['메뉴를 골라보세요.', '영화 제목으로 검색', '카테고리 별로 보기']
    movie_id_titles_df = pd.read_csv('Movie_Id_Titles')
    select_menu = st.selectbox('무엇을 기준으로 영화를 찾으시겠습니까?', menu)
    if select_menu == '영화 제목으로 검색':
        search_title()
    elif select_menu == '카테고리 별로 보기':
        search_category()
    else:
        pass

#영화 제목으로 검색하기
def search_title():
    searched_title = st.text_input('영화 제목을 입력하세요')
    if len(searched_title) != 0:
        
        searched_title_df = movie_id_titles_df.loc[movie_id_titles_df['title'].str.lower().str.contains(searched_title.lower()) == True,]['title']

        if sum(movie_id_titles_df.loc[movie_id_titles_df['title'].str.lower().str.contains(searched_title.lower())) != 0:
            find_title = searched_title_df.iloc[0]
        else:
            pass



        if len(find_title) != 0:
            st.success('찾으신 영화 제목은 \"{}\"인 것 같습니다.'.format(find_title))
        else:
            st.failure('찾으신 ')

            
    else:
        pass


#카테고리별로 보기.
#데이터 프레임 자체를 화면에 띄워야하는데 컬럼명 보이는 게 사용자 입장에서 보기 안좋을 듯해서 한글로 바꿨다.
#일주일 만에 와서 보는데, 컬럼 이름을 한글로 바꿔놓고 사용하고 있어서 다 '카테고리를 고르세요' 이런 문구인 줄 알았다.
def search_category():
    menu = ['리뷰 수', '평균 별점', '리뷰 수 + 평균 별점']
    select_category = st.selectbox('카테고리를 고르세요.', menu)   #멀티셀렉트 박스로 바꾸기. + 표 사이즈 계속 바뀌지 않는 게 뭐가 있었는데.
    if select_category == '리뷰 수':

        radio_option = ['내림차순', '오름차순']
        select_sort = st.radio('오름차순 내림차순을 고르세요', radio_option )

        if select_sort == '내림차순':
            sort_by_customer = False
        elif select_sort == '오름차순':
            sort_by_customer = True
        else:
            pass

        st.dataframe(movie_review_count_rating.loc[:, ['title' , 'review_counts']].sort_values('review_counts', ascending = sort_by_customer))

    elif select_category == '평균 별점':

        radio_option = ['내림차순', '오름차순']
        select_sort = st.radio('오름차순 내림차순을 고르세요', radio_option )

        if select_sort == '내림차순':
            sort_by_customer = False
        elif select_sort == '오름차순':
            sort_by_customer = True
        else:
            pass
        st.dataframe(movie_review_count_rating.loc[:, ['title' , 'average_rating']].sort_values('average_rating', ascending = sort_by_customer))

    elif select_category == '리뷰 수 + 평균 별점':
        pass

        st.dataframe(movie_review_count_rating.loc[:,].sort_values('average_rating', ascending = False))

    else:
        pass


    
