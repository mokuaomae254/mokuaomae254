import streamlit as st
import matplotlib.pyplot as plt

st.header("Portfolio Design and Risk Management")

income = st.number_input("Enter your annual income:")
investment = income * 0.1
st.text("Invest 10% of your income, or $" + str(investment) + ", in crypto.")

if income <= 100:
    st.text("Allocate 20% of your portfolio to layer 0 and 80% to layer 1.")
    labels = 'layer 0', 'layer 1'
    sizes = [20, 80]
    mycolors = ["yellow", "hotpink"]
    explode = (0, 0.1) 
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, colors = mycolors)
    ax1.axis('equal')  
    st.pyplot(fig1)
elif income > 100 and income <= 1000:
    st.text("Allocate 30% of your portfolio to layer 0 and 70% to layer 1.")
    labels = 'layer 0', 'layer 1'
    sizes = [30, 70]
    mycolors = ["yellow", "hotpink"]
    explode = (0, 0.1) 
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, colors = mycolors)
    ax1.axis('equal')  
    st.pyplot(fig1)
elif income > 1000 and income <= 10000:
    st.text("Allocate 40% of your portfolio to layer 0 and 60% to layer 1.")
    labels = 'layer 0', 'layer 1'
    sizes = [40, 60]
    mycolors = ["yellow", "hotpink"]
    explode = (0, 0.1) 
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, colors = mycolors)
    ax1.axis('equal')  
    st.pyplot(fig1)
elif income > 10000 and income <= 100000:
    st.text("Allocate 50% of your portfolio to layer 0 and 50% to layer 1.")
    labels = 'layer 0', 'layer 1'
    sizes = [50, 50]
    mycolors = ["yellow", "hotpink"]
    explode = (0, 0.1) 
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, colors = mycolors)
    ax1.axis('equal')  
    st.pyplot(fig1)
elif income > 100000 and income <= 1000000:
    st.text("Allocate 60% of your portfolio to layer 0 and 40% to layer 1.")
    labels = 'layer






import streamlit as st
import matplotlib.pyplot as plt

st.header("Portfolio Design and Risk Management")

income = st.number_input("Enter your annual income:")
investment = income * 0.1
st.text("Invest 10% of your income, or $" + str(investment) + ", in crypto.")

if income <= 100:
st.text("Allocate 20% of your portfolio to crypto and 80% to conservative investments.")
labels = 'CRYPTO', 'CONSERVATIVE'
sizes = [20, 80]
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
st.text("Allocate 40% of your portfolio to crypto and 60% to conservative investments.")
labels = 'CRYPTO', 'CONSERVATIVE'
sizes = [40, 60]
mycolors = ["yellow", "hotpink"]
explode = (0, 0.1)
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, colors = mycolors)
ax1.axis('equal')
st.pyplot(fig1)

elif income > 10000 and income <= 100000:
st.text("Allocate 50% of your portfolio to crypto and 50% to conservative investments.")
labels = 'CRYPTO', 'CONSERVATIVE'
sizes = [50, 50]
mycolors = ["yellow", "hotpink"]
explode = (0, 0.1)
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, colors = mycolors)
ax1.axis('equal')
st.pyplot(fig1)

elif income > 100000 and income <= 1000000:
st.text("Allocate 60% of your portfolio to crypto and 40% to

rewrite the code with layer 1 having 30% and layer 0,layer 2 and layer 3 to be equal


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



import streamlit as st
import matplotlib.pyplot as plt

st.header("Portfolio Design and Risk Management")

income = st.number_input("Enter your annual income:")
investment = income * 0.1
st.text("Invest 10% of your income, or $" + str(investment) + ", in crypto.")

if income <= 100:
    st.text("Allocate 30% of your portfolio to layer 1 and the remaining 70% to be equally allocated among layer 0, layer 2 and layer 3.")
    labels = 'LAYER 1', 'LAYER 0', 'LAYER 2', 'LAYER 3'
    sizes = [30, 10, 20, 40]
    mycolors = ["yellow", "hotpink", "purple", "green"]
    explode = (0, 0, 0, 0)
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, colors = mycolors)
    ax1.axis('equal')
    st.pyplot(fig1)

elif income > 100 and income <= 1000:
    st.text("Allocate 30% of your portfolio to layer 1 and the remaining 70% to be equally allocated among layer 0, layer 2 and layer 3.")
    labels = 'LAYER 1', 'LAYER 0', 'LAYER 2', 'LAYER 3'
    sizes = [30, 10, 20, 40]
    mycolors = ["yellow", "hotpink", "purple", "green"]
    explode = (0, 0, 0, 0)
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, colors = mycolors)
    ax1.axis('equal')
    st.pyplot(fig1)

elif income > 1000 and income <= 10000:
    st.text("Allocate 30% of your portfolio to layer 1 and the remaining 70% to be equally allocated among layer 0, layer 2 and layer 3.")
    labels = 'LAYER 1', 'LAYER 0', 'LAYER 2', 'LAYER 3'
    sizes = [30, 10, 20, 40]
    mycolors = ["yellow", "hotpink", "purple", "green"]
    explode = (0, 0, 0, 0)
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, colors = mycolors)
    ax1.axis('equal')
    st.pyplot(fig1)
