import pandas as pd
import numpy as np
import streamlit as st
import requests

#cert_path = 'path/to/your/certificate.pem'
r = requests.get("https://cryptoslate.com/coins/", verify=False)
#r = requests.get("https://cryptoslate.com/coins/", verify=cert_path)
dataframe = pd.read_html(r.text)[0]
dataframe = dataframe[["Name","Price","24H %","24H %","24H %","7D %","30D %","ATH","% ATH"]]

dataframe["Name"] = dataframe["Name"].apply(lambda x: x.split("  ")[0]) # modify elements(entries) in x
dataframe["Price"] = dataframe["Price"].apply(lambda x:x.replace(",","").replace("$",""))

dataframe['24H %'] = dataframe['24H %'].str.replace(',', '').str.replace('$', '')
dataframe["24H %"] = pd.to_numeric(dataframe["24H %"]).abs()
dataframe["24H %"] = dataframe["24H %"].str.replace(',', '').str.replace('$', '')
dataframe["24H %"] = pd.to_numeric(dataframe["24H %"]).abs()
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

investor_confidence=[ ]
for index in dataframe.index:
        if (dataframe.loc[dataframe['Name'].isin(['Bitcoin BTC'])], dataframe["24H %"][index])<(dataframe["24H %"][index])<=5:
            investor_confidence.append("very low IC")

        elif (dataframe.loc[dataframe['Name'].isin(['Bitcoin BTC'])],dataframe["24H %"][index])<(dataframe["24H %"][index])<=10:
            investor_confidence.append(" low IC")
        elif (dataframe.loc[dataframe['Name'].isin(['Bitcoin BTC'])],dataframe["24H %"][index])<(dataframe["24H %"][index])<=15:
            investor_confidence.append("medium IC") 
        
        elif (dataframe.loc[dataframe['Name'].isin(['Bitcoin BTC'])],dataframe["24H %"][index])<(dataframe["24H %"][index])<=20:
            
            investor_confidence.append("high IC")
        elif (dataframe.loc[dataframe['Name'].isin(['Bitcoin BTC'])],dataframe["24H %"][index])<(dataframe["24H %"][index])<=25:
            investor_confidence.append("very high IC")
        elif (dataframe.loc[dataframe['Name'].isin(['Bitcoin BTC'])],dataframe["24H %"][index])<(dataframe["24H %"][index])<=30:
            investor_confidence.append("extremely high IC")
        
dataframe['investor_confidence'] = investor_confidence
dataframe.loc[dataframe['Name'].isin(['Tether USDT','USD Coin USDC','Binance USD BUSD','Dai DAI','Paxos Standard USDP','TrueUSD TUSD','USDD USDD','Neutrino USD USDN','Gemini Dollar GUSD']), 'investor_confidence'] = 'stablecoin'
st.dataframe(dataframe)
#streamlit run full_scrap.py
#satoshi 100 index data58.csv
#streamlit run liquid.py
#streamlit run investor_confidence2.py
""" 
import pandas as pd
import numpy as np
import streamlit as st
import requests

#cert_path = 'path/to/your/certificate.pem'
r = requests.get("https://cryptoslate.com/coins/", verify=False)
#r = requests.get("https://cryptoslate.com/coins/", verify=cert_path)
dataframe = pd.read_html(r.text)[0]
dataframe = dataframe[["Name","Price","24H %","24H %","24H %","7D %","30D %","ATH","% ATH"]]

dataframe["Name"] = dataframe["Name"].apply(lambda x: x.split("  ")[0]) # modify elements(entries) in x
dataframe["Price"] = dataframe["Price"].apply(lambda x:x.replace(",","").replace("$",""))

dataframe['24H %'] = dataframe['24H %'].str.replace(',', '').str.replace('$', '')
dataframe["24H %"] = pd.to_numeric(dataframe["24H %"]).abs()
dataframe["24H %"] = dataframe["24H %"].str.replace(',', '').str.replace('$', '')
dataframe["24H %"] = pd.to_numeric(dataframe["24H %"]).abs()
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

investor_confidence=[ ]
for index in dataframe.index:
        if (dataframe.loc[dataframe['Name'].isin(['Bitcoin BTC'])], dataframe["24H %"][index])<(dataframe["24H %"][index])<=5:
            investor_confidence.append("very low IC")

        elif (dataframe.loc[dataframe['Name'].isin(['Bitcoin BTC'])],dataframe["24H %"][index])<(dataframe["24H %"][index])<=10:
            investor_confidence.append(" low IC")
        elif (dataframe.loc[dataframe['Name'].isin(['Bitcoin BTC'])],dataframe["24H %"][index])<(dataframe["24H %"][index])<=15:
            investor_confidence.append("medium IC") 
        
        elif (dataframe.loc[dataframe['Name'].isin(['Bitcoin BTC'])],dataframe["24H %"][index])<(dataframe["24H %"][index])<=20:
            
            investor_confidence.append("high IC")
        elif (dataframe.loc[dataframe['Name'].isin(['Bitcoin BTC'])],dataframe["24H %"][index])<(dataframe["24H %"][index])<=25:
            investor_confidence.append("very high IC")
        elif (dataframe.loc[dataframe['Name'].isin(['Bitcoin BTC'])],dataframe["24H %"][index])<(dataframe["24H %"][index])<=30:
            investor_confidence.append("extremely high IC")
        
dataframe['investor_confidence'] = investor_confidence
dataframe.loc[dataframe['Name'].isin(['Tether USDT','USD Coin USDC','Binance USD BUSD','Dai DAI','Paxos Standard USDP','TrueUSD TUSD','USDD USDD','Neutrino USD USDN','Gemini Dollar GUSD']), 'investor_confidence'] = 'stablecoin'
st.dataframe(dataframe)
#streamlit run full_scrap.py
#satoshi 100 index data58.csv
#streamlit run liquid.py
#streamlit run investor_confidence2.py  based on this code implement an if ....else that checks if Bitcoin BTC is down -30% and any other name is up 30% on the day excluding Bitcoin BTC and print out "extremely high confidence" elif Bitcoin BTC is down between -20 to -25% and any name is up 20-25% on the day print out "very high confidence" elif Bitcoin BTC is down between -15 to -20% and any name is up 15-20% on the day print out " high confidence" elif Bitcoin BTC is down between -10 to -15% and any name is up 10-15% on the day print out "medium confidence" elif Bitcoin BTC is down between -5 to -10% and any name is up 5-10% on the day print out "low confidence" elif Bitcoin BTC is down between 0 to -5% and any name is up 0-5% on the day print out "very low  confidence"
The code is a web scraping script that retrieves cryptocurrency information from the website "https://cryptoslate.com/coins/", parses it into a Pandas DataFrame and performs data cleaning operations on the resulting DataFrame.

It then creates a new column in the DataFrame called "investor_confidence" by checking the percentage change of the cryptocurrency price in 24 hours. If the percentage change is between certain values, it assigns corresponding investor confidence levels (very low, low, medium, high, very high, extremely high) to each row in the "investor_confidence" column.

For stablecoins, such as Tether, the script assigns "stablecoin" as the investor confidence level. Finally, the script uses the Streamlit library to display the resulting DataFrame in a web interface.
"""