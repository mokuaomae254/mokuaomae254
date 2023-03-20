import schedule
import time
import pandas as pd
import numpy as np
import streamlit as st
import requests

def scraping_script():
    r = requests.get("https://cryptoslate.com/coins/", verify=True)
    dataframe = pd.read_html(r.text)[0]
    dataframe.index.name = "rank"
    dataframe = dataframe[["Name","Price","Market Cap","24H Vol","24H %","7D %","30D %","ATH","% ATH"]]

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

    data=dataframe.to_csv("satoshi 100 index data58.csv",index=True )
    st.dataframe(data)
    dataframe.index.name = "rank"
    dataframe=pd.read_csv("satoshi 100 index data58.csv")
    liquidity_risk=[ ]
    for index in dataframe.index:
            if (dataframe["24H Vol"][index])<(dataframe["Market Cap"][index]*0.05):
                liquidity_risk.append("illiquid")

            elif (dataframe["24H Vol"][index])>(dataframe["Market Cap"][index]*0.05) and (dataframe["24H Vol"][index])<=(dataframe["Market Cap"][index]*0.1):
                liquidity_risk.append("fairly liquid")
                ...
            elif (dataframe["24H Vol"][index]) > (dataframe["Market Cap"][index] * 0.1) and (dataframe["24H Vol"][index]) <= (dataframe["Market Cap"][index] * 0.3 ):
                liquidity_risk.append("highly liquid") 
            elif (dataframe["24H Vol"][index]) > (dataframe["Market Cap"][index] * 0.3) and (dataframe["24H Vol"][index]) <= (dataframe["Market Cap"][index] * 0.5):
                liquidity_risk.append("limited long term potential")
            elif (dataframe["24H Vol"][index]) > (dataframe["Market Cap"][index] * 0.5):
                liquidity_risk.append("high liquidity risk")
    dataframe["liquidity_risk"] = liquidity_risk
    return dataframe

    st.set_page_config(page_title="Cryptocurrency Data", page_icon=":guardsman:", layout="wide")
    data = None
    status_text = st.empty()

    def update_data():
        global data
        data = scraping_script()
        status_text.success("Data updated successfully!")

    update_data()
    schedule.every(2).minutes.do(update_data)
    scraping_script()

    if data is not None:
        st.dataframe(data)

    while True:
        schedule.run_pending()
        time.sleep(1)
#st.dataframe(data)
#streamlit run script_automation.py
"""
import schedule
import time

def scraping_script():
    # your scraping code here

schedule.every(10).minutes.do(scraping_script)

while True:
    schedule.run_pending()
    time.sleep(1)



$$$$$$$
    ...
        elif (dataframe["24H Vol"][index]) > (dataframe["Market Cap"][index] * 0.1) and (dataframe["24H Vol"][index]) <= (dataframe["Market Cap"][index] * 0.3 ):
            liquidity_risk.append("highly liquid") 
        elif (dataframe["24H Vol"][index]) > (dataframe["Market Cap"][index] * 0.3) and (dataframe["24H Vol"][index]) <= (dataframe["Market Cap"][index] * 0.5):
            liquidity_risk.append("limited long term potential")
        elif (dataframe["24H Vol"][index]) > (dataframe["Market Cap"][index] * 0.5):
            liquidity_risk.append("high liquidity risk")
    dataframe["liquidity_risk"] = liquidity_risk
    return dataframe

st.set_page_config(page_title="Cryptocurrency Data", page_icon=":guardsman:", layout="wide")
data = None
status_text = st.empty()

def update_data():
    global data
    data = scraping_script()
    status_text.success("Data updated successfully!")

update_data()
schedule.every(10).minutes.do(update_data)

if data is not None:
    st.dataframe(data)

while True:
    schedule.run_pending()
    time.sleep(1)

"""