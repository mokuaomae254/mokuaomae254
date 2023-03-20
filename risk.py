import pandas as pd
import numpy as np
import streamlit as st

dataframe=pd.read_csv("satoshi 100 index data26.csv")
liquidity_risk = []
for index in dataframe.index:
    if (dataframe["24H Vol"][index]) < (dataframe["Market Cap"][index] * 0.05):
        liquidity_risk.append("illiquid")
    elif (dataframe["24H Vol"][index]) > (dataframe["Market Cap"][index] * 0.05) and (dataframe["24H Vol"][index]) <= (dataframe["Market Cap"][index] * 0.1):
        liquidity_risk.append("fairly liquid")
    elif (dataframe["24H Vol"][index]) > (dataframe["Market Cap"][index] * 0.1) and (dataframe["24H Vol"][index]) <= (dataframe["Market Cap"][index] * 0.3 ):
        liquidity_risk.append("highly liquid") 
    elif (dataframe["24H Vol"][index]) > (dataframe["Market Cap"][index] * 0.3) and (dataframe["24H Vol"][index]) <= (dataframe["Market Cap"][index] * 0.5):
        liquidity_risk.append("limited long term potential")
    elif (dataframe["24H Vol"][index]) > (dataframe["Market Cap"][index] * 0.5):
        liquidity_risk.append("stay off")

dataframe['liquidity_risk'] = liquidity_risk

st.dataframe(dataframe)
#streamlit run risk.py
