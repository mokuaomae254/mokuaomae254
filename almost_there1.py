import streamlit as st
import pandas as pd
import numpy as np
import matplotlib
import streamlit as st
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
#import beautifulsoup4 as bs
import requests
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
def ageis18():
    import streamlit as st
    import matplotlib.pyplot as plt
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'CRYPTO', 'SP500', 'DJIA', 'NASDAQ'
    sizes = [50, 16.67, 16.67, 16.67]
    explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.pyplot(fig1)
#streamlit run pie_chart.py
def ageis18_30():
    import streamlit as st
    import matplotlib.pyplot as plt
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'CRYPTO', 'SP500', 'DJIA', 'NASDAQ'
    sizes = [50, 16.67, 16.67, 16.67]
    explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.pyplot(fig1)

def ageis30_40():
    import streamlit as st
    import matplotlib.pyplot as plt
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'CRYPTO', 'SP500', 'DJIA', 'NASDAQ'
    sizes = [40, 20, 20, 20]
    explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.pyplot(fig1)
def ageis40_50():
    import streamlit as st
    import matplotlib.pyplot as plt
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'CRYPTO', 'SP500', 'DJIA', 'NASDAQ'
    sizes = [30, 23.33, 23.33, 23.33]
    explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.pyplot(fig1)

def ageis50_60():
    import streamlit as st
    import matplotlib.pyplot as plt
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'CRYPTO', 'SP500', 'DJIA', 'NASDAQ'
    sizes = [20, 26.67, 26.67, 26.67]
    explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.pyplot(fig1)
def ageis60_70():
    import streamlit as st
    import matplotlib.pyplot as plt
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'CRYPTO', 'SP500', 'DJIA', 'NASDAQ'
    sizes = [10, 30, 30, 30]
    explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.pyplot(fig1)

def ageis70_200():
    import streamlit as st
    import matplotlib.pyplot as plt
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'CRYPTO', 'SP500', 'DJIA', 'NASDAQ'
    sizes = [5, 31.67, 31.67, 31.67]
    explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
def macro_is_king():
    import streamlit as st
    import matplotlib.pyplot as plt
    from PIL import Image
    image = Image.open('Screenshot (32).png')
    image2 = Image.open('Screenshot (34).png')
    st.text("MACRO IS KING")
    st.image(image, caption='UNITED STATES CPI INFLATION DATA')
    st.image(image2, caption='UNITED STATES CORE INFLATION DATA')
    #streamlit run inflation_data.py
    #st.pyplot(fig1)
# NOTE: This must be the first command in your app, and must be set only once
st.set_page_config(layout="wide")
tab1, tab2, tab3,tab4,tab5,tab6,tab7,tab8 = st.tabs(["RISK DISCLAIMER","Top 100 Cryptocurrencies","Macro Analysis", "Sentiment Analysis", "portfolio design and risk management","Altcoin Season Index","Onchain Analysis","Investor Connect"])
with tab1:
   st.header("RISK DISCLAIMER")
   
   st.text(" \n\r       Before deciding to participate in the Crypto market,you should carefully consider your investment objectives, \n\rlevel of experience and risk appetite.Most importantly, do not invest money you cannot afford to lose.\n\rCrypto trading is very risky and you may lose all or some of your investments. \n\rAll the information, analyses, opinions, news, research, prices, or other information  are provided as general market commentary,\n\rand do not constitute or imply any investment advice.\n\rUnder no circumstances will OpenCipher  accept any liability for any loss or damage, including, any loss of profit, \n\rwhich may arise directly or indirectly from the use of or complete reliance on information contained in the given articles or in any analyses.")

with tab2:
   st.header("Top 100 Cryptocurrencies")
   data=pd.read_csv("satoshi 100 index data26.csv")
   st.dataframe(data)
   
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab3:
   st.header("Macro Analysis")
   macro_is_king()
   
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab4:
   st.header("Sentiment Analysis")
   myindicator()

with tab5:
   st.header("portfolio design and risk management")
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
    ageis18()
    #myindicator()
        
   elif age>18 and age<=30:
    #print("allocate 50% of your portfolio to BTC")
    st.text("PORTFOLIO DESIGN AND RISK MANAGEMENT")
    st.text("allocate 50% of your portfolio to crypto and 50 % between the SP500,DJIA and NASDAQ indices")
    ageis18_30()
    #myindicator()
   elif age>30 and age<=40:
    #print("allocate 40% of your portfolio to BTC")
    st.text("PORTFOLIO DESIGN AND RISK MANAGEMENT")
    st.text("allocate 40% of your portfolio to crypto and 60 % between the SP500,DJIA and NASDAQ indices")
    ageis30_40()
    #myindicator()
   elif age>40 and age<=50:
    #print("allocate 30% of your portfolio to BTC")
    st.text("PORTFOLIO DESIGN AND RISK MANAGEMENT")
    st.text("allocate 30% of your portfolio to crypto and 70 % between the SP500,DJIA and NASDAQ indices")
    ageis40_50()
    #myindicator()

   elif age>50 and age<=60:
    #print("allocate 20% of your portfolio to BTC")
    st.text("PORTFOLIO DESIGN AND RISK MANAGEMENT")
    st.text("allocate 20% of your portfolio to crypto and 80 % between the SP500,DJIA and NASDAQ indices")
    ageis50_60()
    #myindicator()
    
   elif age>60 and age<=70:
    #print("allocate 10% of your portfolio to BTC")
    st.text("PORTFOLIO DESIGN AND RISK MANAGEMENT")
    st.text("allocate 10% of your portfolio to crypto and 90 % between the SP500,DJIA and NASDAQ indices")
    ageis60_70()
    #myindicator()   
    
   elif age>70 and age<=200:
    #print("allocate 5% of your portfolio to BTC")
    st.text("PORTFOLIO DESIGN AND RISK MANAGEMENT")
    st.text("allocate 5% of your portfolio to crypto and 95 % between the SP500,DJIA and NASDAQ indices")
    ageis70_200()
    #myindicator()
    
   else:
    print("can not access the model.")
    
   #st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
with tab6:
   st.header("Altcoin Season Index")
   st.text("Coming Soon")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
   
with tab7:
   st.header("Onchain Analysis")
   st.text("Coming Soon")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
with tab8:
   st.header("Investor Connect")
   st.text("What is on your watchlist this month?")
   st.text("Coming Soon")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)



#streamlit run almost_there1.py
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



plt.show()
#streamlit run almost_there1.py