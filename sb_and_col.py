import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

data={
    st.header("Macro Analysis")
    #import streamlit as st
    
    #time.sleep(10)
    
    image = Image.open('Screenshot (32).png')
    image2 = Image.open('Screenshot (34).png')
    st.text("MACRO IS KING")
    st.image(image, caption='UNITED STATES CPI INFLATION DATA')
    st.image(image2, caption='UNITED STATES CORE INFLATION DATA')
    
}
df=pd.dataframe(data=data)
col=st.sidebar.selectbox("Data Visualization",("core inflation","CPI inflation") )
    
st.image(data)


# streamlit run sb_and_col.py