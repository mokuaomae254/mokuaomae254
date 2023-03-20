import pandas as pd
import numpy as np
import streamlit as st
import requests
import schedule
import time

filename = "satoshi 100 index data58.csv"

def scraping_script():
    global filename
    
    r=requests.get("https://cryptoslate.com/coins/", verify=False)
    dataframe=pd.read_html(r.text)[0]
    dataframe.index.name = "rank"
    dataframe=dataframe[["Name","Price","Market Cap","24H Vol","24H %","7D %","30D %","ATH","% ATH"]]

    dataframe["Name"]=dataframe["Name"].apply(lambda x: x.split("  ")[0])
    dataframe["Price"]=dataframe["Price"].apply(lambda x:x.replace(",","").replace("$",""))

    dataframe['Market Cap'] = dataframe['Market Cap'].str.replace(',', '').str.replace('$', '')
    dataframe["Market Cap"] = pd.to_numeric(dataframe["Market Cap"]).abs()
    dataframe["24H Vol"]=dataframe["24H Vol"].str.replace(',', '').str.replace('$', '')
    dataframe["24H Vol"] = pd.to_numeric(dataframe["24H Vol"]).abs()
    dataframe["ATH"]=dataframe["ATH"].str.replace(',', '').str.replace('$', '')

    dataframe["24H %"]=dataframe["24H %"].str.replace('%', '')
    dataframe["24H %"] = pd.to_numeric(dataframe["24H %"])
    dataframe["7D %"]=dataframe["7D %"].str.replace('%', '')
    dataframe["7D %"] = pd.to_numeric(dataframe["7D %"])
    dataframe["30D %"]=dataframe["30D %"].str.replace('%', '')
    dataframe["30D %"] = pd.to_numeric(dataframe["30D %"])
    dataframe["% ATH"]=dataframe["% ATH"].str.replace('%', '')
    dataframe["% ATH"] = pd.to_numeric(dataframe["% ATH"])

    # Append new data to CSV file
    with open(filename, mode='a') as file:
        dataframe.to_csv(file, header=file.tell()==0)

    # Read updated CSV file into dataframe
    dataframe=pd.read_csv(filename, index_col="rank")
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
    dataframe.loc[dataframe['Name'].isin(['Tether USDT','USD Coin USDC','Binance USD BUSD','Dai DAI','Paxos Standard USDP','TrueUSD TUSD','USDD USDD','Neutrino USD USDN','Gemini Dollar GUSD']), 'liquidity_risk'] = 'stablecoin'
    st.dataframe(dataframe)

schedule.every(1).seconds.do(scraping_script)

    
while True:
    schedule.run_pending()
    
    time.sleep(1)
    scraping_script()
#streamlit run automation_test3.py     