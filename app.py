import streamlit as st
import gdown
import pickle
import requests


# Download files
gdown.download(f"https://drive.google.com/uc?id=1z8Hk3B1BplBpPfVw8FlESgs14WsAP5kK", "movies_list.pkl", quiet=False)
gdown.download(f"https://drive.google.com/uc?id=1gDEZFamsB19alNh8FAzZGnK1sRqbLCUb", "similarity.pkl", quiet=False)

# https://drive.google.com/file/d/1z8Hk3B1BplBpPfVw8FlESgs14WsAP5kK/view?usp=sharing
# https://drive.google.com/file/d/1gDEZFamsB19alNh8FAzZGnK1sRqbLCUb/view?usp=sharing

# Load files
movies = pickle.load(open("movies_list.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

movies_list=movies['title'].values

st.header("Movie Recommender System")
selectvalue = st.selectbox("Select movie from dropdown",movies_list)


def recommend(movie):
    index=movies[movies['title']==movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
    recommend_movie=[]
    for i in distance[1:6]:
        recommend_movie.append(movies.iloc[i[0]].title)
    return recommend_movie



if st.button("Show Recommend"):
    movie_name= recommend(selectvalue)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(movie_name[0])
    with col2:
        st.text(movie_name[1])
    with col3:
        st.text(movie_name[2])
    with col4:
        st.text(movie_name[3])
    with col5:
        st.text(movie_name[4])


