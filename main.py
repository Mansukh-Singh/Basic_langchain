import streamlit as st
from langchain_helper import generate_response
import wikipedia

st.title("Singer Name")

text = st.sidebar.selectbox("Pick a text",("pollywood","bollywood","hollywood","tollywood"))

if text:
    answer = generate_response(text)
    st.write("Type : ",answer['text'])
    st.write("Artist : ",answer['artist_name'].strip('\n'))
    st.write("date_of_birth : ",answer['dob'])