""" This code uses Streamlit to display the plot instead of using plt.show() at the end. The st.set_style("dark") sets the background of the plot to dark and st.pyplot() to show the plot."""
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import ta


#st.set_style("dark")

df = pd.read_csv("BCHAIN-MKPRU.csv")[["Date","Value"]]
df.Date = pd.to_datetime(df.Date)
df = df[df.Value > 0]
df.sort_values(by="Date", inplace=True)

fig, (ax1, ax2) = plt.subplots(2, sharex=True)
ax1.semilogy(df.Date, df.Value,linewidth=0.5)
df["rsi"] = ta.momentum.rsi(close=df.Value, window=14)

ax2.axhline(50.47, color="red",linewidth=1.0)

ax2.text(df.Date.iloc[-1], 85, 'Bull Market', fontsize=8, rotation=0,
         ha='left', va='center',color='blue',
         bbox=dict(boxstyle='round', ec='k', fc='w'))
ax2.text(df.Date.iloc[-1], 15, 'Bear Market', fontsize=8, rotation=0,
         ha='left', va='center',color='blue',
         bbox=dict(boxstyle='round', ec='k', fc='w'))


ax2.plot(df.Date, df.rsi,linewidth=0.5)
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()
#streamlit run momentum_strat.py




#streamlit run bull_bear.py