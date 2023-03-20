import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image

st.header("Investor Connect")
st.text("Share your charts below")
username = st.text_input("Enter your username")
caption = st.text_input("What is the chart about")
uploaded_files = st.file_uploader("Choose one or more files", accept_multiple_files=True)



if uploaded_files is not None:
    
    for uploaded_file in uploaded_files:
        st.write("Posted by " + username)
        image = Image.open(uploaded_file)
        st.image(image, caption=caption)

#streamlit run investor_connect2.py