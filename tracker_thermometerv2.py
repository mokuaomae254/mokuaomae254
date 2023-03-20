import pandas as pd
import numpy as np
import matplotlib
import streamlit as st
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
#import beautifulsoup4 as bs
import requests
data=pd.read_csv("satoshi 100 index data27.csv")


st.text("RISK DISCLAIMER. \n\r       Before deciding to participate in the Crypto market,\n\ryou should carefully consider your investment objectives, \n\rlevel of experience and risk appetite. \n\r       Most importantly, do not invest money you cannot afford to lose.\n\rCrypto trading is very risky and you may lose all or some of your investments. \n\rAll the information, analyses, opinions, news, research, prices, or \n\rother information  are provided as general market commentary,\n\rand do not constitute or imply any investment advice.\n\r        Under no circumstances will OpenCipher  accept any liability for \n\rany loss or damage, including, any loss of profit, \n\rwhich may arise directly or indirectly from the use of\n\r or complete reliance on information contained \n\rin the given articles or in any analyses.")

st.dataframe(data)

def myindicator():
    import pandas as pd
    import matplotlib.pyplot as plt
    matplotlib.use('TkAgg')
   
    

    dataframe = pd.read_csv("BCHAIN-MKPRU.csv")
    dataframe = dataframe.iloc[::-1]
    dataframe['200wma'] = dataframe['Value'].rolling(window = 1400).mean()

    dataframe = dataframe[1400:]
    dates = pd.to_datetime(dataframe['Date'])

    monthly = dataframe[::30]

    distance = monthly['200wma'].pct_change() * 100





    plt.style.use("dark_background")

    plt.semilogy(dates, dataframe['Value'], color = "grey", zorder = 1)
    plt.semilogy(dates, dataframe['200wma'], color = "purple", zorder = 2)

    
    plt.scatter(monthly['Date'], monthly['Value'], c = distance, cmap = 'rainbow', vmin = 0, vmax = 16, zorder = 4 )
    
    cbar = plt.colorbar()
    cbar.set_label("% monthly increase in 200wma")
    cbar.ax.yaxis.set_label_position("left")
    
   
    st.set_option('deprecation.showPyplotGlobalUse', False)

    st.pyplot( )
age= st.number_input("enter your age:")    

if age==18:
    
    st.text("you are of age.")
    
    st.text("PORTFOLIO DESIGN AND RISK MANAGEMENT")
    st.text("allocate 50% of your portfolio to crypto and 50 % between the SP500,DJIA and NASDAQ indices")
  
    myindicator()
        
elif age>18 and age<=30:
   
    st.text("PORTFOLIO DESIGN AND RISK MANAGEMENT")
    st.text("allocate 50% of your portfolio to crypto and 50 % between the SP500,DJIA and NASDAQ indices")
   
    myindicator()
elif age>30 and age<=40:
    
    st.text("PORTFOLIO DESIGN AND RISK MANAGEMENT")
    st.text("allocate 40% of your portfolio to crypto and 60 % between the SP500,DJIA and NASDAQ indices")
   
    myindicator()
elif age>40 and age<=50:
    
    st.text("PORTFOLIO DESIGN AND RISK MANAGEMENT")
    st.text("allocate 30% of your portfolio to crypto and 70 % between the SP500,DJIA and NASDAQ indices")
    
    myindicator()

elif age>50 and age<=60:
    
    st.text("PORTFOLIO DESIGN AND RISK MANAGEMENT")
    st.text("allocate 20% of your portfolio to crypto and 80 % between the SP500,DJIA and NASDAQ indices")
    
    myindicator()
    
elif age>60 and age<=70:
    
    st.text("PORTFOLIO DESIGN AND RISK MANAGEMENT")
    st.text("allocate 10% of your portfolio to crypto and 90 % between the SP500,DJIA and NASDAQ indices")
  
    myindicator()
    
elif age>70 and age<=200:
    
    st.text("PORTFOLIO DESIGN AND RISK MANAGEMENT")
    st.text("allocate 5% of your portfolio to crypto and 95 % between the SP500,DJIA and NASDAQ indices")
    
    myindicator()
    
else:
    print("can not access the model.")
    
#streamlit run tracker_thermometerv2.py
    