
import streamlit as st
import matplotlib.pyplot as plt
    #time.sleep(10)
from PIL import Image
#image = Image.open('MM4_Investor_sentiment_V3 (1).jpg')
image2 = Image.open('20200317-the-psychology-of-a-market-cycle.png')
image3 = Image.open('saupload_manias_bubbles.jpg')
st.text("MACRO IS KING")
#st.image(image, caption='UNITED STATES CPI INFLATION DATA')
st.image(image2, caption='UNITED STATES CORE INFLATION DATA')
st.image(image3, caption='UNITED STATES CORE INFLATION DATA')

#streamlit run sentiment.py