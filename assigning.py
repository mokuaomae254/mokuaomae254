# importing pandas as pd
import pandas as pd
import numpy as np
import streamlit as st
# Making data frame from the csv file

dataframe=pd.read_csv("satoshi 100 index data24.csv")
result=[ ]
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
            result=print("yes")
#print(result)
        
  #streamlit run liquidity_risk.py
            

# Printing the first 10 rows of
# the data frame for visualization
#df[:10]
# increase the salary by 10 %

data=dataframe.assign(liquidity_risk = lambda x: dataframe['%ATH'] + result)
st.dataframe(data)
#streamlit run assigning.py