import pandas as pd
import matplotlib
import streamlit as st
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')


data=pd.read_csv("satoshi 100 index data24.csv")
#print(data)
st.dataframe(data)
st.image("bitcoin heatmap.png", width=500)

#streamlit run market_thermometerv1.py