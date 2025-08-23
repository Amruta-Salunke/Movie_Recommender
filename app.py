import streamlit as st
import pickle
import requests

movies = pickle.load(open('moives_list.pkl','rb'))

st.header("Movie Recommender System")
st.selectbox("Select movie from dropdown",movies)

if st.button("Show recommend"):
     pass
