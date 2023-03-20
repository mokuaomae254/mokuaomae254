import pandas as pd
import numpy as np
import streamlit as st
import requests
def investor():
    #cert_path = 'path/to/your/certificate.pem'
    r = requests.get("https://cryptoslate.com/coins/", verify=False)
    #r = requests.get("https://cryptoslate.com/coins/", verify=cert_path)
    dataframe = pd.read_html(r.text)[0]
    dataframe = dataframe[["Name","Price","24H %","24H %","24H %","7D %","30D %","ATH","% ATH"]]

    dataframe["Name"] = dataframe["Name"].apply(lambda x: x.split("  ")[0]) # modify elements(entries) in x
    dataframe["Price"] = dataframe["Price"].apply(lambda x:x.replace(",","").replace("$",""))

    dataframe['24H %'] = dataframe['24H %'].str.replace(',', '').str.replace('$', '')
    dataframe["24H %"] = pd.to_numeric(dataframe["24H %"]).abs()
    dataframe["ATH"] = dataframe["ATH"].str.replace(',', '').str.replace('$', '')

    # TO add % comment
    dataframe["24H %"] = dataframe["24H %"].str.replace('%', '')
    dataframe["24H %"] = pd.to_numeric(dataframe["24H %"])
#dataframe=pd.read_csv("satoshi 100 index data58.csv")
dataframe=pd.read_csv("df_combined.csv")
investor_confidence = []
for index in dataframe.index:
    if dataframe.loc[dataframe['Name'] == 'Bitcoin BTC', '24H %'].iloc[0] >= -30:
        if dataframe.loc[(dataframe['Name'] != 'Bitcoin BTC') & (dataframe['24H %'] >= 30)].shape[0] > 0:
            investor_confidence.append("extremely high IC")
    elif dataframe.loc[dataframe['Name'] == 'Bitcoin BTC', '24H %'].iloc[0] >= -20 and dataframe.loc[dataframe['Name'] == 'Bitcoin BTC', '24H %'].iloc[0] <= -30:
        if dataframe.loc[(dataframe['Name'] != 'Bitcoin BTC') & (dataframe['24H %'] >= 20) & (dataframe['24H %'] < 30)].shape[0] > 0:
            investor_confidence.append("very high IC")
    elif dataframe.loc[dataframe['Name'] == 'Bitcoin BTC', '24H %'].iloc[0] >= -15 and dataframe.loc[dataframe['Name'] == 'Bitcoin BTC', '24H %'].iloc[0] <= -20:
        if dataframe.loc[(dataframe['Name'] != 'Bitcoin BTC') & (dataframe['24H %'] >= 15) & (dataframe['24H %'] < 20)].shape[0] > 0:
            investor_confidence.append("high IC")
    elif dataframe.loc[dataframe['Name'] == 'Bitcoin BTC', '24H %'].iloc[0] >= -10 and dataframe.loc[dataframe['Name'] == 'Bitcoin BTC', '24H %'].iloc[0] <= -15:
        if dataframe.loc[(dataframe['Name'] != 'Bitcoin BTC') & (dataframe['24H %'] >= 10) & (dataframe['24H %'] < 15)].shape[0] > 0:
            investor_confidence.append("moderate IC")
    elif dataframe.loc[dataframe['Name'] == 'Bitcoin BTC', '24H %'].iloc[0] >= -5 and dataframe.loc[dataframe['Name'] == 'Bitcoin BTC', '24H %'].iloc[0] <= -10:
        if dataframe.loc[(dataframe['Name'] != 'Bitcoin BTC') & (dataframe['24H %'] >= 5) & (dataframe['24H %'] < 10)].shape[0] > 0:
            investor_confidence.append("low IC")
    else:
        investor_confidence.append("bear market ")

dataframe["Investor Confidence"] = investor_confidence
st.write(dataframe)
#streamlit run ic_trial.py
#Version 
#pip install streamlit==1.17.0


