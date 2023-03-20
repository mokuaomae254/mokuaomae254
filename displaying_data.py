import pandas as pd
import streamlit as st
import numpy as np

data=pd.read_csv("satoshi 100 index data24.csv")
#print(data)
st.dataframe(data)
#streamlit run displaying_data.py
