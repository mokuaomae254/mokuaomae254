import pandas as pd
import numpy as np
import streamlit as st

import base64
from io import BytesIO
from matplotlib.backends.backend_pdf import FigureCanvasPdf as FigureCanvas

#from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

#st.header("Top 100 Cryptocurrencies By Market Capitalization")
    #dataframe = dataframe.drop(columns=["ATH","% ATH"], axis=1)

dataframe=pd.read_csv("satoshi 100 index data58.csv")
#st.dataframe(data)
dataframe.index.name = "rank"
#converting column to list
#dataframe=pd.read_csv("satoshi 100 index data58.csv")
liquidity_risk=[ ]
for index in dataframe.index:
        if (dataframe["24H Vol"][index])<(dataframe["Market Cap"][index]*0.05):
            liquidity_risk.append("illiquid")

        elif (dataframe["24H Vol"][index])>(dataframe["Market Cap"][index]*0.05) and (dataframe["24H Vol"][index])<=(dataframe["Market Cap"][index]*0.1):
            liquidity_risk.append("fairly liquid")
        elif (dataframe["24H Vol"][index]) > (dataframe["Market Cap"][index] * 0.1) and (dataframe["24H Vol"][index]) <= (dataframe["Market Cap"][index] * 0.3 ):
            liquidity_risk.append("highly liquid") 
        
        elif (dataframe["24H Vol"][index]) > (dataframe["Market Cap"][index] * 0.3) and (dataframe["24H Vol"][index]) <= (dataframe["Market Cap"][index] * 0.5):
            
            liquidity_risk.append("limited long term potential")
        elif (dataframe["24H Vol"][index]) > (dataframe["Market Cap"][index] * 0.5):
            liquidity_risk.append("stay off")
        
dataframe['liquidity_risk'] = liquidity_risk
dataframe.loc[dataframe['Name'].isin(['Tether USDT','USD Coin USDC','Binance USD BUSD','Dai DAI','Paxos Standard USDP','TrueUSD TUSD','USDD USDD','Neutrino USD USDN','Gemini Dollar GUSD',"cDAI. cdai","cUSDC. cusdc"]), 'liquidity_risk'] = 'stablecoin'
#st.dataframe(dataframe)


    #streamlit run downloading_report.py
#dataframe = pd.read_csv("satoshi 100 index data58.csv")
#dataframe = pd.read_csv("satoshi 100 index data31.csv")
#st.header("Top 100 Cryptocurrencies")
st.header("Cryptocurrency Market Daily,Weekly and Monthly Report ")
#data=pd.read_csv("satoshi 100 index data29.csv")
#st.dataframe(dataframe)
   
#print(df)
i=0
st.subheader("Today's Winners ")
for i in range(10):
    
    data=dataframe.sort_values(by=['24H %'], ascending=False)
st.dataframe(data)
df = pd.DataFrame(data)

if st.button("Download CSV1"):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="mydata.csv">Download CSV File</a>'
    st.markdown(href, unsafe_allow_html=True)
#csv_downloader()
st.subheader("Today's Biggest Losers ")
for i in range(10):
    
    data=dataframe.sort_values(by=['24H %'])
st.dataframe(data)
df = pd.DataFrame(data)

if st.button("Download CSV2"):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="mydata.csv">Download CSV File</a>'
    st.markdown(href, unsafe_allow_html=True)
#csv_downloader()
st.subheader("This week's Winners ")
for i in range(10):
   
    data=dataframe.sort_values(by=['7D %'], ascending=False)
st.dataframe(data)
df = pd.DataFrame(data)

if st.button("Download CSV3"):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="mydata.csv">Download CSV File</a>'
    st.markdown(href, unsafe_allow_html=True)
#csv_downloader()
st.subheader("This week's Biggest lossers ")
for i in range(10):
    
    data=dataframe.sort_values(by=['7D %'])
st.dataframe(data)
df = pd.DataFrame(data)

if st.button("Download CSV4"):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="mydata.csv">Download CSV File</a>'
    st.markdown(href, unsafe_allow_html=True)
#csv_downloader()
st.subheader("This Month's Winners ")
for i in range(10):
    
    data=dataframe.sort_values(by=['30D %'], ascending=False)
st.dataframe(data)
df = pd.DataFrame(data)

if st.button("Download CSV5"):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="mydata.csv">Download CSV File</a>'
    st.markdown(href, unsafe_allow_html=True)
#csv_downloader()
st.subheader("This Month's Biggest Losers ")
for i in range(10):
    
    data=dataframe.sort_values(by=['30D %'])
st.dataframe(data)
df = pd.DataFrame(data)

if st.button("Download CSV6"):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="mydata.csv">Download CSV File</a>'
    st.markdown(href, unsafe_allow_html=True)
#csv_downloader()
#streamlit run report_lidrisk.py