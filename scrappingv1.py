import pandas as pd
import numpy as np
import streamlit as st

import requests

r=requests.get("https://cryptoslate.com/coins/",verify=False)
dataframe=pd.read_html(r.text)[0]
dataframe=dataframe[["Name","Price","Market Cap","24H Vol","24H %","7D %","30D %","ATH","% ATH"]]

dataframe["Name"]=dataframe["Name"].apply(lambda x: x.split("  ")[0])#modify elements(entries) in x
dataframe["Price"]=dataframe["Price"].apply(lambda x:x.replace(",","").replace("$",""))

dataframe['Market Cap'] = dataframe['Market Cap'].str.replace(',', '').str.replace('$', '')
dataframe["24H Vol"]=dataframe["24H Vol"].str.replace(',', '').str.replace('$', '')
dataframe["ATH"]=dataframe["ATH"].str.replace(',', '').str.replace('$', '')
#TO add % comment 
dataframe["24H %"]=dataframe["24H %"].str.replace('%', '')
dataframe["7D %"]=dataframe["7D %"].str.replace('%', '')
dataframe["30D %"]=dataframe["30D %"].str.replace('%', '')
dataframe["% ATH"]=dataframe["% ATH"].str.replace('%', '')

dataframe.to_csv("satoshi 100 index data26.csv",index=True )#index true 0-99

data=pd.read_csv("satoshi 100 index data26.csv")

st.text("RISK DISCLAIMER. \n\rBefore deciding to participate in the Crypto market,\n\r  you should carefully consider your investment objectives, \n\rlevel of experience and risk appetite. \n\rMost importantly, do not invest money you cannot afford to lose.\n\r FOREX trading is very risky and you may lose all or some of your investments. \n\rAll the information, analyses, opinions, news, research, prices, or \n\rother information  \n\rare provided as general market commentary,\n\r and do not constitute or imply any investment advice.\n\r Under no circumstances will OpenCipher \n\r accept any liability for any loss or damage, \n\rincluding, any loss of profit,\n\r which may arise directly or indirectly from the use of\n\r or complete reliance on information\n\r contained in the given articles or in any analyses.")

st.dataframe(data)

def myindicator():
    import pandas as pd
    import matplotlib.pyplot as plt
    matplotlib.use('TkAgg')
   
    #age=int(input("enter your age:"))

    dataframe = pd.read_csv("BCHAIN-MKPRU.csv")
    dataframe = dataframe.iloc[::-1]
    dataframe['200wma'] = dataframe['Value'].rolling(window = 1400).mean()
#df['300wma'] = df['Value'].rolling(window = 1400).mean()
    dataframe = dataframe[1400:]
    dates = pd.to_datetime(dataframe['Date'])

    monthly = dataframe[::30]

    distance = monthly['200wma'].pct_change() * 100

#distance = monthly['300wma'].pct_change() * 100



    plt.style.use("dark_background")

    plt.semilogy(dates, dataframe['Value'], color = "grey", zorder = 1)
    plt.semilogy(dates, dataframe['200wma'], color = "purple", zorder = 2)
#plt.semilogy(dates, df['300wma'], color = "green", zorder = 3)

    plt.scatter(monthly['Date'], monthly['Value'], c = distance, cmap = 'rainbow', vmin = 0, vmax = 16, zorder = 4 )

    cbar = plt.colorbar()
    cbar.set_label("% monthly increase in 200wma")
    cbar.ax.yaxis.set_label_position("left")

    st.set_option('deprecation.showPyplotGlobalUse', False)

    st.pyplot()

age= st.number_input("enter your age:")    
#age=int(input("enter your age:"))
#print("your age is",age)
#age=18
if age==18:
    #print("you are of age.")
    st.text("you are of age.")
    #print("allocate 50% of your portfolio to BTC")
    st.text("allocate 50% of your portfolio to crypto and 50 % between the SP500,DJIA and NASDAQ indices")
    myindicator()
        
elif age>18 and age<=30:
    #print("allocate 50% of your portfolio to BTC")
    st.text("allocate 50% of your portfolio to crypto and 50 % between the SP500,DJIA and NASDAQ indices")
    myindicator()
elif age>30 and age<=40:
    #print("allocate 40% of your portfolio to BTC")
    st.text("allocate 40% of your portfolio to crypto and 60 % between the SP500,DJIA and NASDAQ indices")
    myindicator()
elif age>40 and age<=50:
    #print("allocate 30% of your portfolio to BTC")
    st.text("allocate 30% of your portfolio to crypto and 70 % between the SP500,DJIA and NASDAQ indices")
    myindicator()

elif age>50 and age<=60:
    #print("allocate 20% of your portfolio to BTC")
    st.text("allocate 20% of your portfolio to crypto and 80 % between the SP500,DJIA and NASDAQ indices")
    myindicator()
    
elif age>60 and age<=70:
    #print("allocate 10% of your portfolio to BTC")
    st.text("allocate 10% of your portfolio to crypto and 90 % between the SP500,DJIA and NASDAQ indices")
    myindicator()
    
elif age>70 and age<=200:
    #print("allocate 5% of your portfolio to BTC")
    st.text("allocate 5% of your portfolio to crypto and 95 % between the SP500,DJIA and NASDAQ indices")
    myindicator()
    
else:
    print("can not access the model.")
    
