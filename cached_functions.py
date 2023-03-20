import streamlit as st
import pandas as pd 
st.set_page_config(layout="wide")
import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image

@st.cache(suppress_st_warning=True)
def sentiment_analysis():
    image2 = Image.open('20200317-the-psychology-of-a-market-cycle.png')
    image3 = Image.open('saupload_manias_bubbles.jpg')
    st.image(image2, caption='EMOTIONAL ROLLERCOASTER.1')
    st.image(image3, caption='EMOTIONAL ROLLERCOASTER.2')
@st.cache(suppress_st_warning=True)
def crypto_portfolio():
	import streamlit as st
	import matplotlib.pyplot as plt

	#st.header("Portfolio Design and Risk Management")
	st.subheader("Crypto portfolio")

	income = st.number_input("Enter your annual income:")
	investment = income * 0.1
	st.text("Invest 10% of your income, or $" + str(investment) + ", in crypto.")

	if income > 100 :
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
		st.text("consult with Hedge Funds,private Equity Firms or Venture Capitals as you are regarded as an accredited investor An accredited investor is an individual or entity that meets certain financial and income criteria as established by the Securities and Exchange Commission (SEC). The criteria are intended to identify individuals and entities that have the financial sophistication and ability to bear the economic risks of investing in securities that are not registered with the SEC. Examples of accredited investors include individuals with a net worth of over $1 million (excluding the value of their primary residence), or an annual income of over $200,000 for the past two years (or $300,000 when combined with a spouse). Institutions such as banks, insurance companies, and investment companies also qualify as accredited investors.")
	else:
		st.text("The minimum amount you can buy in an exchange is 10 USD")	
	#"""streamlit run crypto_portfolio.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import ta
from functools import lru_cache

@lru_cache(maxsize=None)
def dca():
    """ This code uses Streamlit to display the plot instead of using plt.show() at the end. The st.set_style("dark") sets the background of the plot to dark and st.pyplot() to show the plot."""
    import streamlit as st
    import pandas as pd
    import matplotlib.pyplot as plt
    import ta
    
    def dca_strat():
        import streamlit as st
        import pandas as pd

        st.title("Dollar Cost Averaging Strategy for Bitcoin")

        # Load data for bitcoin prices
        df = pd.read_csv("BCHAIN-MKPRU.csv")
        df.Date = pd.to_datetime(df.Date)
        df = df[df.Value > 0] # remove rows with closing price of 0 or less
        df.sort_values(by="Date", inplace=True)

        # Get user input for investment amount and interval
        investment_amount = st.number_input("Enter investment amount:", min_value=1, step=1)
        investment_interval = st.number_input("Enter investment interval (in days):", min_value=1, step=1)

        # Get user input for start and end date
        start_date = pd.to_datetime(st.date_input("Enter start date:"))
        end_date = pd.to_datetime(st.date_input("Enter end date:"))

        # Filter dataframe to include only rows within the start and end date range
        df = df[(df.Date >= start_date) & (df.Date <= end_date)]

        # Initialize variables to keep track of investment
        investment_count = 0
        total_invested = 0
        shares_bought = 0

        # Validation check for investment amount
        if investment_amount < 10:
            st.error("Investment amount must be greater than $10")
        else:
            # Iterate through the data and make investments at the specified intervals
            for index, row in df.iterrows():
                if investment_count % investment_interval == 0:
                    # Make investment
                    investment_count = 0
                    shares_bought += investment_amount / row["Value"]
                    total_invested += investment_amount
                    st.write("Bought {:.8f} BTC for ${} on {}".format(investment_amount/row["Value"], investment_amount, row["Date"]))
                investment_count += 1

            # Print total invested and final value of investment
            if df.empty:
                st.warning("No data within the specified date range")
            else:
                final_value = shares_bought * row["Value"]
                st.write("Total invested: ${}".format(total_invested))
                st.write("Final value of investment: {:.2f}".format(final_value))

    #st.set_style("dark")

    df = pd.read_csv("BCHAIN-MKPRU.csv")[["Date","Value"]]
    df.Date = pd.to_datetime(df.Date)
    df = df[df.Value > 0]
    df.sort_values(by="Date", inplace=True)

    fig, (ax1, ax2) = plt.subplots(2, sharex=True)
    ax1.semilogy(df.Date, df.Value,linewidth=0.5)
    df["rsi"] = ta.momentum.rsi(close=df.Value, window=14)
    ax2.axhline(80, color="yellow",linewidth=0.8)
    ax2.axhline(95, color="red",linewidth=0.8)
    #ax2
    ax2.axhline(25, color="green",linewidth=0.8)
    ax2.axhline(10, color="green",linewidth=0.8)
    ax2.text(df.Date.iloc[-1], 85, 'Take Profit', fontsize=8, rotation=0,
            ha='left', va='center',color='blue',
            bbox=dict(boxstyle='round', ec='k', fc='w'))
    ax2.text(df.Date.iloc[-1], 15, 'Build a position', fontsize=8, rotation=0,
            ha='left', va='center',color='blue',
            bbox=dict(boxstyle='round', ec='k', fc='w'))
    if df["rsi"].iloc[-1] > 80:
        # Sell/DCA out
        st.write("RSI is above 80, time to sell/DCA out")
        dca_strat()
        
    elif df["rsi"].iloc[-1] < 20:
        # Buy/DCA in
        st.write("RSI is below 20, time to buy/DCA in")
        dca_strat()
        
    else:
        st.write("RSI is between 20 and 80, hold position")


    ax2.plot(df.Date, df.rsi,linewidth=0.5)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import ta
from functools import lru_cache

@lru_cache(maxsize=None)

def dca_strat():
    st.title("Dollar Cost Averaging Strategy for Bitcoin")

    # Load data for bitcoin prices
    df = pd.read_csv("BCHAIN-MKPRU.csv")
    df.Date = pd.to_datetime(df.Date)
    df = df[df.Value > 0] # remove rows with closing price of 0 or less
    df.sort_values(by="Date", inplace=True)

    # Get user input for investment amount and interval
    investment_amount = st.number_input("Enter investment amount:", min_value=1, step=1)
    investment_interval = st.number_input("Enter investment interval (in days):", min_value=1, step=1)

    # Get user input for start and end date
    start_date = pd.to_datetime(st.date_input("Enter start date:"))
    end_date = pd.to_datetime(st.date_input("Enter end date:"))

    # Filter dataframe to include only rows within the start and end date range
    df = df[(df.Date >= start_date) & (df.Date <= end_date)]

    # Initialize variables to keep track of investment
    investment_count = 0
    total_invested = 0
    shares_bought = 0

    # Validation check for investment amount
    if investment_amount < 10:
        st.error("Investment amount must be greater than $10")
    else:
        # Iterate through the data and make investments at the specified intervals
        for index, row in df.iterrows():
            if investment_count % investment_interval == 0:
                # Make investment
                investment_count = 0
                shares_bought += investment_amount / row["Value"]
                total_invested += investment_amount
                st.write("Bought {:.8f} BTC for ${} on {}".format(investment_amount/row["Value"], investment_amount, row["Date"]))
            investment_count += 1

        # Print total invested and final value of investment
        if df.empty:
            st.warning("No data within the specified date range")
        else:
            final_value = shares_bought * row["Value"]
            st.write("Total invested: ${}".format(total_invested))
            st.write("Final value of investment: {:.2f}".format(final_value))

#st.set_style("dark")

df = pd.read_csv("BCHAIN-MKPRU.csv")[["Date","Value"]]
df.Date = pd.to_datetime(df.Date)
df = df[df.Value > 0]
df.sort_values(by="Date", inplace=True)

fig, (ax1, ax2) = plt.subplots(2, sharex=True)
ax1.semilogy(df.Date, df.Value,linewidth=0.5)
df["rsi"] = ta.momentum.rsi(close=df.Value, window=14)
ax2.axhline(80, color="yellow",linewidth=0.8)
ax2.axhline(95, color="red",linewidth=0.8)
#ax2.axhline(50, color="black",linewidth=0.8)
ax2.axhline(25, color="green",linewidth=0.8)
ax2.axhline(10, color="green",linewidth=0.8)
ax2.text(df.Date.iloc[-1], 85, 'Take Profit', fontsize=8, rotation=0,
        ha='left', va='center',color='blue',
        bbox=dict(boxstyle='round', ec='k', fc='w'))
ax2.text(df.Date.iloc[-1], 15, 'Build a position', fontsize=8, rotation=0,
        ha='left', va='center',color='blue',
        bbox=dict(boxstyle='round', ec='k', fc='w'))
if df["rsi"].iloc[-1] > 80:
    # Sell/DCA out
    st.write("RSI is above 80, time to sell/DCA out")
    dca_strat()
    
elif df["rsi"].iloc[-1] < 20:
    # Buy/DCA in
    st.write("RSI is below 20, time to buy/DCA in")
    dca_strat()
    
else:
    st.write("RSI is between 20 and 80, hold position")


ax2.plot(df.Date, df.rsi,linewidth=0.5)
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()
	#streamlit run momentum_strat.py
import streamlit as st
import pandas as pd
import numpy as np
import time
import matplotlib
# import streamlit as st
import matplotlib.pyplot as plt

@st.cache(suppress_st_warning=True)
def topcryptos():
    st.header("Top 100 Cryptocurrencies")

    data=pd.read_csv("satoshi 100 index data58.csv")
    st.dataframe(data)
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import ta

@st.cache
def risk_environment():
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
import pandas as pd
import numpy as np
import streamlit as st
import requests

@st.cache(suppress_st_warning=True)
def scrapping():
    r=requests.get("https://cryptoslate.com/coins/",verify=True)
    dataframe=pd.read_html(r.text)[0]
    dataframe.index.name = "rank"
    dataframe=dataframe[["Name","Price","Market Cap","24H Vol","24H %","7D %","30D %","ATH","% ATH"]]

    dataframe["Name"]=dataframe["Name"].apply(lambda x: x.split("  ")[0])
    dataframe["Price"]=dataframe["Price"].apply(lambda x:x.replace(",","").replace("$",""))

    dataframe['Market Cap'] = dataframe['Market Cap'].str.replace(',', '').str.replace('$', '')
    dataframe["Market Cap"] = pd.to_numeric(dataframe["Market Cap"]).abs()
    dataframe["24H Vol"]=dataframe["24H Vol"].str.replace(',', '').str.replace('$', '')
    dataframe["24H Vol"] = pd.to_numeric(dataframe["24H Vol"]).abs()
    dataframe["ATH"]=dataframe["ATH"].str.replace(',', '').str.replace('$', '')

    dataframe["24H %"]=dataframe["24H %"].str.replace('%', '')
    dataframe["24H %"] = pd.to_numeric(dataframe["24H %"])
    dataframe["7D %"]=dataframe["7D %"].str.replace('%', '')
    dataframe["7D %"] = pd.to_numeric(dataframe["7D %"])
    dataframe["30D %"]=dataframe["30D %"].str.replace('%', '')
    dataframe["30D %"] = pd.to_numeric(dataframe["30D %"])
    dataframe["% ATH"]=dataframe["% ATH"].str.replace('%', '')
    dataframe["% ATH"] = pd.to_numeric(dataframe["% ATH"])


    data=dataframe.to_csv("satoshi 100 index data58.csv",index=True )#index true 0-99
    #st.dataframe(data)
    dataframe.index.name = "rank"
    #converting column to list
    dataframe=pd.read_csv("satoshi 100 index data58.csv")
    liquidity_risk=[ ]
    for index in dataframe.index:
            if (dataframe["24H Vol"][index])<(dataframe["Market Cap"][index]*0.05):
                liquidity_risk.append("illiquid")

            elif (dataframe["24H Vol"][index])>(dataframe["Market Cap"][index]*0.05) and (dataframe["24H Vol"][index])<=(dataframe["Market Cap"][index]*0.1):
                liquidity_risk.append("fairly liquid")
            elif (dataframe["24H Vol"][index]) > (dataframe["Market Cap"][index] * 0.1) and (dataframe["24H Vol"][index]) <= (dataframe["Market Cap"][index] * 0.3 ):
                liquidity_risk.append("highly liquid") 
            
            elif (dataframe["24H Vol"][index]) > (dataframe["Market Cap"][index] * 0.3) and (dataframe["24H Vol"][index]) <= (dataframe["Market Cap"][index] * 0.5):
                
                liquidity_risk.append("limited long term potential")
            elif (dataframe["24H Vol"][index]) > (dataframe["Market Cap"][index] * 0.5):
                liquidity_risk.append("stay off")
            
    dataframe['liquidity_risk'] = liquidity_risk
    dataframe.loc[dataframe['Name'].isin(['Tether USDT','USD Coin USDC','Binance USD BUSD','Dai DAI','Paxos Standard USDP','TrueUSD TUSD','USDD USDD','Neutrino USD USDN','Gemini Dollar GUSD']), 'liquidity_risk'] = 'stablecoin'
    st.dataframe(dataframe)
    #streamlit run full_scrap.py

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
@st.cache(suppress_st_warning=True)
def altcoinseason():
	st.title("Altcoin Season Indicator")

	# Read in dataframe
	dataframe = pd.read_csv("satoshi 100 index data58.csv")
	stablecoins = ['Tether USDT','USD Coin USDC','Binance USD BUSD','Dai DAI','Paxos Standard USDP','TrueUSD TUSD','USDD USDD','Neutrino USD USDN','Gemini Dollar GUSD',"cDAI. cdai","cUSDC. cusdc","cETH. ceth","Wrapped Bitcoin WBTC"]
	dataframe = dataframe[~dataframe['Name'].isin(stablecoins)]
	#Check if the dataframe is empty or not
	if dataframe.empty:
		st.error("Dataframe is empty")
	else:
		# Select top 99 coins
		top_99 = dataframe.head(99)

		# Check if there is "Bitcoin BTC" in the dataframe
		bitcoin_24H_perc = dataframe.loc[dataframe["Name"] == "Bitcoin BTC", "24H %"]
		if bitcoin_24H_perc.empty:
			st.error("Bitcoin BTC not found in dataframe")
		else:
			# Prompt user to input the timeframe
			timeframe = st.selectbox("Select a timeframe:", ["Daily", "Weekly", "Monthly"])

			# Use the selected timeframe to select the appropriate column from the dataframe
			if timeframe == "Daily":
				selected_column = "24H %"
			elif timeframe == "Weekly":
				selected_column = "7D %"
			elif timeframe == "Monthly":
				selected_column = "30D %"
			else:
				st.error("Invalid timeframe selected")
				#return

			# Create a new column that calculates the percentage difference between each coin's selected column and Bitcoin BTC's selected column
			top_99["Difference"] = top_99[selected_column] - bitcoin_24H_perc.values[0]

			# Create a new column that indicates whether each coin outperforms Bitcoin BTC or not
			top_99["Outperforms"] = top_99["Difference"] > 0

			# Count the number of coins that outperform Bitcoin BTC
			outperformers = top_99["Outperforms"].sum()

			# Calculate the percentage of coins that outperform Bitcoin BTC
			percent_outperform = (outperformers / len(top_99)) * 100

			# Create a pie chart to visualize the results
			labels = ["Altcoin Season", "Bitcoin BTC Season"]
			mycolors = ["yellow","b"]
			sizes = [percent_outperform, 100 - percent_outperform]
			st.set_option('deprecation.showPyplotGlobalUse', False)
			plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90,colors=mycolors)
			plt.axis('equal')
			st.pyplot()

			if percent_outperform > 90 and percent_outperform<100:
				st.warning("The altcoins are so overvalued in the timeframe take profits agressively into stablecoins,BTC and ETH")
			elif percent_outperform > 80 and percent_outperform<=90:
				st.warning("Take some profits into BTC,ETH and stablecoins")
			elif percent_outperform > 10 and percent_outperform<=20:
				st.warning("Sell some BTC into altcoins")
			elif percent_outperform > 10 and percent_outperform<=1:
				st.warning("The altcoins are so undervalued in the timeframe sell stablecoins,BTC and ETH gradually into the altcoins")			

sentiment_analysis()
#crypto_portfolio()
#dca()
topcryptos()
risk_environment()
scrapping()
altcoinseason()
#streamlit run cached_functions.py
