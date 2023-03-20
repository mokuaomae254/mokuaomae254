import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)

# Read in data
df = pd.read_csv('BCHAIN-MKPRU.csv')

# Create the chart
plt.plot(df['Date'], df['Value'])

# Add moving averages
plt.plot(df['Date'], df['Value'].rolling(window=8).mean())
#plt.plot(df['Date'], df['Value'].rolling(window=13).mean())
#plt.plot(df['Date'], df['Value'].rolling(window=21).mean())
#plt.plot(df['Date'], df['Value'].rolling(window=55).mean())
#plt.plot(df['Date'], df['Value'].rolling(window=200).mean())

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Bitcoin Chart with Moving Averages')

# Display the chart
st.pyplot()

#streamlit run mas.py