import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

#age=int(input("enter your age:"))

df = pd.read_csv("BCHAIN-MKPRU.csv")
df = df.iloc[::-1]
df['200wma'] = df['Value'].rolling(window = 1400).mean()
df['300wma'] = df['Value'].rolling(window = 1400).mean()
df = df[1400:]
dates = pd.to_datetime(df['Date'])

monthly = df[::30]

distance = monthly['200wma'].pct_change() * 100

#distance = monthly['300wma'].pct_change() * 100



plt.style.use("dark_background")

plt.semilogy(dates, df['Value'], color = "grey", zorder = 1)
plt.semilogy(dates, df['200wma'], color = "purple", zorder = 2)
#plt.semilogy(dates, df['300wma'], color = "green", zorder = 3)

#plt.scatter(monthly['Date'], monthly['Value'], c = distance, cmap = 'rainbow', vmin = 0, vmax = 16, zorder = 4 )

cbar = plt.colorbar()
cbar.set_label("% monthly increase in 200wma")
cbar.ax.yaxis.set_label_position("left")

#st.set_option('deprecation.showPyplotGlobalUse', False)

#st.pyplot( )

#plt.show()
#streamlit run color_indicator.py