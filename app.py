import streamlit as st
import gdown
import pickle
import requests



def fetch_poster(movie_id):
     url = "https://api.themoviedb.org/3/movie/{}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US".format(movie_id)
     data=requests.get(url)
     data=data.json()
     poster_path = data['poster_path']
     full_path = "https://image.tmdb.org/t/p/w500/"+poster_path
     return full_path



# Download files
gdown.download(f"https://drive.google.com/uc?id=1z8Hk3B1BplBpPfVw8FlESgs14WsAP5kK", "movies_list.pkl", quiet=False)
#gdown.download(f"https://drive.google.com/uc?id=1L_A9IeVb5O0F0Pzvrujsev4vzFPexv2i", "similarity.pkl", quiet=False)

import urllib.request

url = "https://drive.usercontent.google.com/download?id=1L_A9IeVb5O0F0Pzvrujsev4vzFPexv2i&export=download"
urllib.request.urlretrieve(url, "similarity.pkl")



# https://drive.google.com/file/d/1z8Hk3B1BplBpPfVw8FlESgs14WsAP5kK/view?usp=sharing
# https://drive.google.com/file/d/1gDEZFamsB19alNh8FAzZGnK1sRqbLCUb/view?usp=sharing
#https://drive.google.com/file/d/1L_A9IeVb5O0F0Pzvrujsev4vzFPexv2i/view?usp=sharing

# Load files
movies = pickle.load(open("movies_list.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

movies_list=movies['title'].values

st.header("Movie Recommender System")




selectvalue = st.selectbox("Select movie from dropdown",movies_list)


# def recommend(movie):
#     index=movies[movies['title']==movie].index[0]
#     distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
#     recommend_movie=[]
#     for i in distance[1:6]:
#         recommend_movie.append(movies.iloc[i[0]].title)
#     return recommend_movie
def recommend(movie):
    index=movies[movies['title']==movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
    recommend_movie=[]
    recommend_poster=[]
    for i in distance[1:6]:
        movies_id=movies.iloc[i[0]].id
        recommend_movie.append(movies.iloc[i[0]].title)
        recommend_poster.append(fetch_poster(movies_id))
    return recommend_movie, recommend_poster


# if st.button("Show Recommend"):
#     movie_name= recommend(selectvalue)
#     col1,col2,col3,col4,col5=st.columns(5)
#     with col1:
#         st.text(movie_name[0])
#     with col2:
#         st.text(movie_name[1])
#     with col3:
#         st.text(movie_name[2])
#     with col4:
#         st.text(movie_name[3])
#     with col5:
#         st.text(movie_name[4])


if st.button("Show Recommend"):
    movie_name, movie_poster = recommend(selectvalue)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(movie_name[0])
        st.image(movie_poster[0])
    with col2:
        st.text(movie_name[1])
        st.image(movie_poster[1])
    with col3:
        st.text(movie_name[2])
        st.image(movie_poster[2])
    with col4:
        st.text(movie_name[3])
        st.image(movie_poster[3])
    with col5:
        st.text(movie_name[4])
        st.image(movie_poster[4])
