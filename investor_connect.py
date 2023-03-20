import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image

st.header("Investor Connect")
st.text("Share your charts below")
username = st.text_input("Enter your username")
caption=st.text_input("What is the chart about")
uploaded_file = st.file_uploader("Choose a file")
st.write("Posted by " + username)
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption=""+caption)
    


#streamlit run investor_connect.py