import streamlit as st
import pickle
import requests

movies = pickle.load(open('moives_list.pkl','rb'))

movies_list=movies['title'].values


st.header("Movie Recommender System")
st.selectbox("Select movie from dropdown",movies_list)


if st.button("Show Recommend"):
     pass
