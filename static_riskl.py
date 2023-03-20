def topcryptos():
    import streamlit as st
    import pandas as pd
    import numpy as np
    import time
    import matplotlib
    #import streamlit as st
    import matplotlib.pyplot as plt
    matplotlib.use('TkAgg')
    st.header("Top 100 Cryptocurrencies By Market Capitalization")
     #dataframe = dataframe.drop(columns=["ATH","% ATH"], axis=1)

    dataframe=pd.read_csv("satoshi 100 index data58.csv")
    #st.dataframe(data)
    
    #dataframe.reset_index(inplace=True,drop=True)
    #dataframe.reset_index(inplace=True)
    #dataframe["index"] = dataframe.index
    dataframe.index.name = "rank"
    dataframe.reset_index(inplace=True,drop=True)
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
    st.dataframe(dataframe)
    #streamlit run full_scrap.py
#streamlit run  static_riskl.py
topcryptos()