import pandas as pd
import numpy as np
import matplotlib
import streamlit as st
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
#import beautifulsoup4 as bs
import requests

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

    return st.pyplot(fig1)
#streamlit run pie_chart.py
st.cache(suppress_st_warning= True)
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

    return st.pyplot(fig1)
st.cache(suppress_st_warning= True)
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

    return st.pyplot(fig1)
st.cache(suppress_st_warning= True)    
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

    return st.pyplot(fig1)
st.cache(suppress_st_warning= True)
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

    return st.pyplot(fig1)
st.cache(suppress_st_warning = True)    
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

    return st.pyplot(fig1)
st.cache(suppress_st_warning= True)

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

    return st.pyplot(fig1)


    


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
    
#streamlit run makeup.py
    