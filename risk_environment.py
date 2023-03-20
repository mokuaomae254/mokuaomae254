""" This code uses Streamlit to display the plot instead of using plt.show() at the end. The st.set_style("dark") sets the background of the plot to dark and st.pyplot() to show the plot."""
""""import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import ta

df = pd.read_csv("BCHAIN-MKPRU.csv")[["Date","Value"]]
df.Date = pd.to_datetime(df.Date)
df = df[df.Value > 0]
df.sort_values(by="Date", inplace=True)

fig, (ax1, ax2) = plt.subplots(2, sharex=True)
ax1.semilogy(df.Date, df.Value,linewidth=0.5)
df["rsi"] = ta.momentum.rsi(close=df.Value, window=14)



ax2.plot(df.Date, df.rsi,linewidth=0.5)
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()"""
#streamlit run momentum_strat.py
#streamlit run risk_environment.py
"""
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import ta

df = pd.read_csv("BCHAIN-MKPRU.csv")[["Date","Value"]]
df.Date = pd.to_datetime(df.Date)
df = df[df.Value > 0]
df.sort_values(by="Date", inplace=True)

fig, ax = plt.subplots()
ax.semilogy(df.Date, df.Value, linewidth=0.5)

st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()
"""
"""
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import ta

df = pd.read_csv("BCHAIN-MKPRU.csv")[["Date","Value"]]
df.Date = pd.to_datetime(df.Date)
df = df[df.Value > 0]
df.sort_values(by="Date", inplace=True)

# Calculate the 200-day moving average
df["ma"] = df["Value"].rolling(window=200).mean()

fig, ax = plt.subplots()
ax.semilogy(df.Date, df.Value, linewidth=0.5)
ax.plot(df.Date, df.ma, color='red', linewidth=1)

st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()
"""
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import ta

df = pd.read_csv("BCHAIN-MKPRU.csv")[["Date","Value"]]
df.Date = pd.to_datetime(df.Date)
df = df[df.Value > 0]
df.sort_values(by="Date", inplace=True)

# Calculate the 200-day moving average
df["ma"] = df["Value"].rolling(window=200).mean()

fig, ax = plt.subplots()
ax.semilogy(df.Date, df.Value, linewidth=0.5)
ax.plot(df.Date, df.ma, color='red', linewidth=1)

st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()

# Check if the Bitcoin price is above the 200-day moving average
if df.Value.iloc[-1] > df.ma.iloc[-1]:
    st.write("Welcome to the bull market!")
else:
    st.write("Welcome to the bear market!")
