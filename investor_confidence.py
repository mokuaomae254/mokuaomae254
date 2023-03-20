import pandas as pd
import numpy as np
import streamlit as st
import requests

#cert_path = 'path/to/your/certificate.pem'
r = requests.get("https://cryptoslate.com/coins/", verify=False)
#r = requests.get("https://cryptoslate.com/coins/", verify=cert_path)
dataframe = pd.read_html(r.text)[0]
dataframe = dataframe[["Name","Price","Market Cap","24H Vol","24H %","7D %","30D %","ATH","% ATH"]]

dataframe["Name"] = dataframe["Name"].apply(lambda x: x.split("  ")[0]) # modify elements(entries) in x
dataframe["Price"] = dataframe["Price"].apply(lambda x:x.replace(",","").replace("$",""))

dataframe['Market Cap'] = dataframe['Market Cap'].str.replace(',', '').str.replace('$', '')
dataframe["Market Cap"] = pd.to_numeric(dataframe["Market Cap"]).abs()
dataframe["24H Vol"] = dataframe["24H Vol"].str.replace(',', '').str.replace('$', '')
dataframe["24H Vol"] = pd.to_numeric(dataframe["24H Vol"]).abs()
dataframe["ATH"] = dataframe["ATH"].str.replace(',', '').str.replace('$', '')

# TO add % comment
dataframe["24H %"] = dataframe["24H %"].str.replace('%', '')
dataframe["24H %"] = pd.to_numeric(dataframe["24H %"])
dataframe["7D %"] = dataframe["7D %"].str.replace('%', '')
dataframe["7D %"] = pd.to_numeric(dataframe["7D %"])
dataframe["30D %"] = dataframe["30D %"].str.replace('%', '')
dataframe["30D %"] = pd.to_numeric(dataframe["30D %"])
dataframe["% ATH"] = dataframe["% ATH"].str.replace('%', '')
dataframe["% ATH"] = pd.to_numeric(dataframe["% ATH"])

# Add new column "Investor Confidence"
dataframe["Investor Confidence"] = np.where((dataframe["24H %"].between(-5, 5)) & 
                                           (dataframe["Name"] != "Bitcoin") & 
                                           (dataframe["Name"] != "Ethereum"), 
                                           "Very Low Investor Confidence", 
                                           "Not Very Low Investor Confidence")

# Print rows with "Very Low Investor Confidence"
low_confidence = dataframe[dataframe["Investor Confidence"] == "Very Low Investor Confidence"]
st.dataframe(low_confidence)

data = dataframe.to_csv("satoshi 100 index data58.csv", index=True) # index true
st.dataframe(data)

#streamlit run investor_confidence.py