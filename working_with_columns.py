import streamlit as st
import pandas as pd
import matplotlib




col1, col2, col3,col4 = st.columns(4,gap="large")
#st.columns(spec, *, gap="small")


with col1:
   st.header("EDUCATION")
   st.image("https://static.streamlit.io/examples/owl.jpg")
with col2:
   st.header("SKILLS")
   st.image("https://static.streamlit.io/examples/owl.jpg")
with col3:
   st.header("PROJECTS")
   st.image("https://static.streamlit.io/examples/owl.jpg")
with col4:
   st.header("CONTACTS")
   st.image("https://static.streamlit.io/examples/owl.jpg")   
#streamlit run working_with_columns.py