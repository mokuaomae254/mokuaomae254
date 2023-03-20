import streamlit as st
import pandas as pd
import numpy as np
import matplotlib

import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
#import beautifulsoup4 as bs
import requests
data=pd.read_csv("satoshi 100 index data26.csv")


st.text("RISK DISCLAIMER. \n\r       Before deciding to participate in the Crypto market,\n\ryou should carefully consider your investment objectives, \n\rlevel of experience and risk appetite. \n\r       Most importantly, do not invest money you cannot afford to lose.\n\rCrypto trading is very risky and you may lose all or some of your investments. \n\rAll the information, analyses, opinions, news, research, prices, or \n\rother information  are provided as general market commentary,\n\rand do not constitute or imply any investment advice.\n\r        Under no circumstances will OpenCipher  accept any liability for \n\rany loss or damage, including, any loss of profit, \n\rwhich may arise directly or indirectly from the use of\n\r or complete reliance on information contained \n\rin the given articles or in any analyses.")

st.dataframe(data)
def macro_is_king():
    from PIL import Image
    image = Image.open('Screenshot (32).png')
    image2 = Image.open('Screenshot (34).png')
    st.text("MACRO IS KING")
    st.image(image, caption='UNITED STATES CPI INFLATION DATA')
    st.image(image2, caption='UNITED STATES CORE INFLATION DATA')
    #streamlit run inflation_data.py
age= st.number_input("enter your age:")    
#age=int(input("enter your age:"))
#print("your age is",age)
#age=18
if age==18:
    #print("you are of age.")
    st.text("you are of age.")
    #print("allocate 50% of your portfolio to BTC")
    st.text("PORTFOLIO DESIGN AND RISK MANAGEMENT")
    st.text("allocate 50% of your portfolio to crypto and 50 % between the SP500,DJIA and NASDAQ indices")
    #ageis18()
    macro_is_king()
    #myindicator()
        
elif age>18 and age<=30:
    #print("allocate 50% of your portfolio to BTC")
    st.text("PORTFOLIO DESIGN AND RISK MANAGEMENT")
    st.text("allocate 50% of your portfolio to crypto and 50 % between the SP500,DJIA and NASDAQ indices")
    #ageis18_30()
    macro_is_king()
    #myindicator()
elif age>30 and age<=40:
    #print("allocate 40% of your portfolio to BTC")
    st.text("PORTFOLIO DESIGN AND RISK MANAGEMENT")
    st.text("allocate 40% of your portfolio to crypto and 60 % between the SP500,DJIA and NASDAQ indices")
    #ageis30_40()
    macro_is_king()
    #myindicator()
elif age>40 and age<=50:
    #print("allocate 30% of your portfolio to BTC")
    st.text("PORTFOLIO DESIGN AND RISK MANAGEMENT")
    st.text("allocate 30% of your portfolio to crypto and 70 % between the SP500,DJIA and NASDAQ indices")
    #ageis40_50()
    macro_is_king()
    #myindicator()

elif age>50 and age<=60:
    #print("allocate 20% of your portfolio to BTC")
    st.text("PORTFOLIO DESIGN AND RISK MANAGEMENT")
    st.text("allocate 20% of your portfolio to crypto and 80 % between the SP500,DJIA and NASDAQ indices")
    #ageis50_60()
    macro_is_king()
    #myindicator()
    
elif age>60 and age<=70:
    #print("allocate 10% of your portfolio to BTC")
    st.text("PORTFOLIO DESIGN AND RISK MANAGEMENT")
    st.text("allocate 10% of your portfolio to crypto and 90 % between the SP500,DJIA and NASDAQ indices")
    #ageis60_70()
    macro_is_king()
    #myindicator()
    
elif age>70 and age<=200:
    #print("allocate 5% of your portfolio to BTC")
    st.text("PORTFOLIO DESIGN AND RISK MANAGEMENT")
    st.text("allocate 5% of your portfolio to crypto and 95 % between the SP500,DJIA and NASDAQ indices")
    #ageis70_200()
    macro_is_king()
    #myindicator()
    
else:
    print("can not access the model.")
#streamlit run inflation_datav4.py