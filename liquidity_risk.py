import pandas as pd
import numpy as np
import streamlit as st
#converting column to list
dataframe=pd.read_csv("satoshi 100 index data58.csv")
#result=[ ]
for index in dataframe.index:
        if (dataframe["24H Vol"][index])<(dataframe["Market Cap"][index]*0.05):
            result=print("illiquid")

        elif (dataframe["24H Vol"][index])>(dataframe["Market Cap"][index]*0.05) and (dataframe["24H Vol"][index])<=(dataframe["Market Cap"][index]*0.1):
            result=print("fairly liquid")

        elif (dataframe["24H Vol"][index])>(dataframe["Market Cap"][index]*0.1)and (dataframe["24H Vol"][index])<=(dataframe["Market Cap"][index]*0.3 ):
            result=print("highly liquid") 
        elif (dataframe["24H Vol"][index])>(dataframe["Market Cap"][index]*0.3) and (dataframe["24H Vol"][index])<=(dataframe["Market Cap"][index]*0.5):
            result=print("limited long term potential")
        elif (dataframe["24H Vol"][index])>(dataframe["Market Cap"][index]*0.5):
            result=print("stay off")

        else:
            print("yes")
#print(result)
st.dataframe(result)        
  #streamlit run liquidity_risk.py
            
    