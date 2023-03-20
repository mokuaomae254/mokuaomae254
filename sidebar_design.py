import streamlit as st
import pandas as pd
import matplotlib

data=pd.read_csv("satoshi 100 index data24.csv")
#print(data)
st.dataframe(data)
# Using object notation
add_selectbox = st.sidebar.selectbox(
    "Data Visualization",
    ("RISK DISCLAIMER","Top_100_Cryptocurrencies","Inflation Data", "Market Thermometer", "portfolio design and risk management","Altcoin Season Index","Buy Crypto")
)

with st.sidebar:
    st.[Top_100_Cryptocurrencies]
    data=pd.read_csv("satoshi 100 index data24.csv")
    st.dataframe(data)
#print(data)
#st.dataframe(data)
    
    

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Were the tools helpfull?",
        ("Yes", "No")
    )
#streamlit run sidebar_design.py
# Object notation
#st.sidebar.[element_name]
# "with" notation
#with st.sidebar:
#    st.[element_name]