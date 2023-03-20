"""
import streamlit as st
import matplotlib.pyplot as plt

st.header("Portfolio Design and Risk Management")

income = st.number_input("Enter your annual income:")
investment = income * 0.1
st.text("Invest 10% of your income, or $" + str(investment) + ", in crypto.")

if income <= 100:
    st.text("Allocate 30% of your portfolio to crypto and 70% to conservative investments.")
    labels = 'CRYPTO', 'CONSERVATIVE'
    sizes = [30, 70]
    mycolors = ["yellow", "hotpink"]
    explode = (0, 0.1)
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, colors = mycolors)
    ax1.axis('equal')
    st.pyplot(fig1)

elif income > 100 and income <= 1000:
    st.text("Allocate 30% of your portfolio to crypto and 70% to conservative investments.")
    labels = 'CRYPTO', 'CONSERVATIVE'
    sizes = [30, 70]
    mycolors = ["yellow", "hotpink"]
    explode = (0, 0.1)
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, colors = mycolors)
    ax1.axis('equal')
    st.pyplot(fig1)

elif income > 1000 and income <= 10000:
    st.text("Allocate 30% of your portfolio to crypto and 70% to conservative investments.")
    labels = 'CRYPTO', 'CONSERVATIVE'
    sizes = [30, 70]
    mycolors = ["yellow", "hotpink"]
    explode = (0, 0.1)
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, colors = mycolors)
    ax1.axis('equal')
    st.pyplot(fig1)

#streamlit run crypto_portfolio.py
"""
import streamlit as st
import matplotlib.pyplot as plt

st.header("Portfolio Design and Risk Management")

income = st.number_input("Enter your annual income:")
investment = income * 0.1
st.text("Invest 10% of your income, or $" + str(investment) + ", in crypto.")

if income <= 100:
    #st.text("Allocate 30% of your portfolio to layer 1 and the remaining 70% to be equally allocated among layer 0, layer 2 and layer 3.")
    labels = 'LAYER 1', 'LAYER 0', 'LAYER 2', 'LAYER 3','INFRA COINS','AI COINS'
    sizes = [30, 10, 20, 20,10,10]
    mycolors = ["yellow", "hotpink", "purple", "green","pink","maroon"]
    explode = (0, 0, 0, 0,0,0)
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, colors = mycolors)
    ax1.axis('equal')
    st.pyplot(fig1)

elif income > 100 and income <= 1000:
    #st.text("Allocate 30% of your portfolio to layer 1 and the remaining 70% to be equally allocated among layer 0, layer 2 and layer 3.")
    labels = 'LAYER 1', 'LAYER 0', 'LAYER 2', 'LAYER 3','INFRA COINS','AI COINS'
    sizes = [10, 20, 20, 20,10,20]
    mycolors = ["yellow", "hotpink", "purple", "green","pink","maroon"]
    explode = (0, 0, 0, 0,0,0)
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, colors = mycolors)
    ax1.axis('equal')
    st.pyplot(fig1)

elif income > 1000 and income <= 10000:
    #st.text("Allocate 30% of your portfolio to layer 1 and the remaining 70% to be equally allocated among layer 0, layer 2 and layer 3.")
    labels = 'LAYER 1', 'LAYER 0', 'LAYER 2', 'LAYER 3','INFRA COINS','AI COINS'
    sizes = [20, 10, 20, 20,20,10]
    mycolors = ["yellow", "hotpink", "purple", "green","pink","maroon"]
    explode = (0, 0, 0, 0,0,0)
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, colors = mycolors)
    ax1.axis('equal')
    st.pyplot(fig1)
elif income > 10000 and income <= 100000:
    #st.text("Allocate 30% of your portfolio to layer 1 and the remaining 70% to be equally allocated among layer 0, layer 2 and layer 3.")
    labels = 'LAYER 1', 'LAYER 0', 'LAYER 2', 'LAYER 3','INFRA COINS','AI COINS'
    sizes = [30, 10, 20, 20,10,10]
    mycolors = ["yellow", "hotpink", "purple", "green","pink","maroon"]
    explode = (0, 0, 0, 0,0,0)
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, colors = mycolors)
    ax1.axis('equal')
    st.pyplot(fig1)
elif income > 100000 and income <= 1000000:
    #st.text("Allocate 30% of your portfolio to layer 1 and the remaining 70% to be equally allocated among layer 0, layer 2 and layer 3.")
    labels = 'LAYER 1', 'LAYER 0', 'LAYER 2', 'LAYER 3','INFRA COINS','AI COINS'
    sizes = [40, 10, 20, 10,10,10]
    mycolors = ["yellow", "hotpink", "purple", "green","pink","maroon"]
    explode = (0, 0, 0, 0,0,0)
    
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, colors = mycolors)
    ax1.axis('equal')
    st.pyplot(fig1)
elif income > 1000000 and income <= 2000000:
    #st.text("Allocate 30% of your portfolio to layer 1 and the remaining 70% to be equally allocated among layer 0, layer 2 and layer 3.")
    labels = 'LAYER 1', 'LAYER 0', 'LAYER 2', 'LAYER 3','INFRA COINS','AI COINS'
    sizes = [50, 10, 10, 10,10,10]
    mycolors = ["yellow", "hotpink", "purple", "green","pink","maroon"]
    explode = (0, 0, 0, 0,0,0)
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, colors = mycolors)
    ax1.axis('equal')
    st.pyplot(fig1)
elif income >  2000000:
    st.text("consult with Hedge Funds,private Equity Firms or Venture Capitals as you are regarded as an accredited investor")
    
#"""streamlit run crypto_portfolio.py