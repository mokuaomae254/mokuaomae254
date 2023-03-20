import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("BCHAIN-MKPRU.csv")[["Date","Value"]]
df["Date"] = pd.to_datetime(df["Date"])
df.sort_values(by="Date", inplace=True)

df.reset_index(inplace=True, drop=True)
df.reset_index(inplace=True)
#df["index"] = df.index

# Calculate metrics
df["btcissuance"] = 7200 / 2**(np.floor(df["index"]/1458))
df["usdissuance"] = df["btcissuance"] * df["Value"]
df["MAusdissuance"] = df["btcissuance"].rolling(window=365).mean()
df = df[df["Date"] >= "2011-01-01"]

# Create plot
fig, ax = plt.subplots()
""" 
ax.fill_between(df["Date"], 4, 10, color="red", alpha=0.4)

ax.fill_between(df["Date"], 0.3, 0.5, color="green", alpha=0.4)
"""
ax2 = ax.twinx()
ax2.semilogy(df["Date"], df["Value"])
ax.semilogy(df["Date"], df["usdissuance"] / df["MAusdissuance"], color="brown")
ax.yaxis.set_major_formatter("{x:1f}")
#ax.yaxis.set_major_formatter("{:.1f}")

ax.yaxis.set_minor_formatter("{x:1f}")
#ax.yaxis.set_minor_formatter("{:.1f}")
# Display DataFrame in Streamlit app

#st.write(df)
st.pyplot(fig)
#streamlit run puell.py