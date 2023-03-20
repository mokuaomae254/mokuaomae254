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
from PIL import Image
image = Image.open('Screenshot (32).png')
image2 = Image.open('Screenshot (34).png')
st.text("MACRO IS KING")
st.image(image, caption='UNITED STATES CPI INFLATION DATA')
st.image(image2, caption='UNITED STATES CORE INFLATION DATA')
#streamlit run inflation_data.py