import streamlit as st
import pandas as pd 
st.set_page_config(layout="wide")
def buy_crypto():
	import streamlit as st
	#st.iframe("https://widget.onramper.com?color=266677&apiKey=pk_test_x5M_5fdXzn1fxK04seu0JgFjGsu7CH8lOvS9xZWzuSM0", width=482, height=660)

	st.markdown("""
	<div style="display: flex; justify-content: center; padding: 15px;">
	<iframe
		style="--border-radius: 10px; box-shadow: 0 2px 10px 0 rgba(0,0,0,.20); border-radius: var(--border-radius); margin: auto;max-width: 420px"
		src="https://widget.onramper.com?color=266677&apiKey=pk_test_x5M_5fdXzn1fxK04seu0JgFjGsu7CH8lOvS9xZWzuSM0"
		height="660px"
		width="482px"
		title="Onramper widget"
		frameborder="0"
		allow="accelerometer; autoplay; camera; gyroscope; payment"
	>
	</iframe>
	</div>
	""", unsafe_allow_html=True)


	#streamlit run onramper.py
	
def crypto_portfolio():
	import streamlit as st
	import matplotlib.pyplot as plt

	st.header("Portfolio Design and Risk Management")
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
def topcryptos():
    import streamlit as st
    import pandas as pd
    import numpy as np
    import time
    import matplotlib
    #import streamlit as st
    import matplotlib.pyplot as plt
    matplotlib.use('TkAgg')
    st.header("Top 100 Cryptocurrencies")
     #dataframe = dataframe.drop(columns=["ATH","% ATH"], axis=1)

    data=pd.read_csv("satoshi 100 index data58.csv")
    st.dataframe(data)
def scrapping():
	import pandas as pd
	import numpy as np
	import streamlit as st
	import requests
	#dataframe.index.name = "rank"
	r=requests.get("https://cryptoslate.com/coins/",verify=True)
	dataframe=pd.read_html(r.text)[0]
	dataframe.index.name = "rank"
	dataframe=dataframe[["Name","Price","Market Cap","24H Vol","24H %","7D %","30D %","ATH","% ATH"]]
	#dataframe = dataframe.drop(columns=[' '], axis=1)

	dataframe["Name"]=dataframe["Name"].apply(lambda x: x.split("  ")[0])#modify elements(entries) in x
	dataframe["Price"]=dataframe["Price"].apply(lambda x:x.replace(",","").replace("$",""))

	dataframe['Market Cap'] = dataframe['Market Cap'].str.replace(',', '').str.replace('$', '')
	dataframe["Market Cap"] = pd.to_numeric(dataframe["Market Cap"]).abs()
	dataframe["24H Vol"]=dataframe["24H Vol"].str.replace(',', '').str.replace('$', '')
	dataframe["24H Vol"] = pd.to_numeric(dataframe["24H Vol"]).abs()
	dataframe["ATH"]=dataframe["ATH"].str.replace(',', '').str.replace('$', '')

	#TO add % comment 
	dataframe["24H %"]=dataframe["24H %"].str.replace('%', '')
	dataframe["24H %"] = pd.to_numeric(dataframe["24H %"])
	dataframe["7D %"]=dataframe["7D %"].str.replace('%', '')
	dataframe["7D %"] = pd.to_numeric(dataframe["7D %"])
	dataframe["30D %"]=dataframe["30D %"].str.replace('%', '')
	dataframe["30D %"] = pd.to_numeric(dataframe["30D %"])
	dataframe["% ATH"]=dataframe["% ATH"].str.replace('%', '')
	dataframe["% ATH"] = pd.to_numeric(dataframe["% ATH"])
 

	data=dataframe.to_csv("satoshi 100 index data58.csv",index=True )#index true 0-99
	st.dataframe(data)
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
def altcoinseason():
	import pandas as pd
	import streamlit as st
	import matplotlib.pyplot as plt

	st.title("Altcoin Season Indicator")

	# Read in dataframe
	dataframe = pd.read_csv("satoshi 100 index data58.csv")

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
			sizes = [percent_outperform, 100 - percent_outperform]
			st.set_option('deprecation.showPyplotGlobalUse', False)
			plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
			plt.axis('equal')
			st.pyplot()

			if percent_outperform > 80:
				st.warning("Take some profits into BTC and ETH")
			elif percent_outperform < 20:
				st.warning("Sell some BTC into altcoins")

def crypto_analytics():
    
	import streamlit as st
	import pandas as pd
	import numpy as np
	import time
	import matplotlib
	#import streamlit as st
	import matplotlib.pyplot as plt
	matplotlib.use('TkAgg')


	#st.set_page_config(layout="wide")
	tab1, tab2, tab3,tab4,tab5,tab6,tab7,tab8,tab9,tab10,tab11 = st.tabs(["RISK DISCLAIMER","Top 100 Cryptocurrencies","Macro Analysis", "Sentiment Analysis", "portfolio design and risk management","Altcoin Season Index","Profit taking","DOLLAR COST AVERAGING","Market Report","investor connect","Buy Crypto"])
	with tab1:
		st.header("RISK DISCLAIMER")
		
		st.text(" \n\r       Before deciding to participate in the Crypto market,you should carefully consider your investment objectives, \n\rlevel of experience and risk appetite.Most importantly, do not invest money you cannot afford to lose.\n\rCrypto trading is very risky and you may lose all or some of your investments. \n\rAll the information, analyses, opinions, news, research, prices, or other information  are provided as general market commentary,\n\rand do not constitute or imply any investment advice.\n\rUnder no circumstances will OpenCipher  accept any liability for any loss or damage, including, any loss of profit, \n\rwhich may arise directly or indirectly from the use of or complete reliance on information contained in the given articles or in any analyses.")

	with tab2:
		st.header("Top 100 Cryptocurrencies")
		data=pd.read_csv("satoshi 100 index data58.csv")
		st.dataframe(data)
		#scrapping()
	
	

	with tab3:
		st.header("Macro Analysis")
		import streamlit as st
		import matplotlib.pyplot as plt
			#time.sleep(10)
		from PIL import Image
		image = Image.open('Screenshot (32).png')
		image2 = Image.open('Screenshot (34).png')
		st.text("MACRO IS KING")
		st.image(image, caption='UNITED STATES CPI INFLATION DATA')
		st.image(image2, caption='UNITED STATES CORE INFLATION DATA')
	
	
	

	with tab4:
		st.header("Sentiment Analysis")
		import pandas as pd
		import matplotlib.pyplot as plt
		matplotlib.use('TkAgg')
		
			
			#time.sleep(10)
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
	

	with tab5:
		st.header("portfolio design and risk management")
		st.subheader("Crypto and the legacy market portfolio")
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
			import streamlit as st
			import matplotlib.pyplot as plt
			#time.sleep(10)
			
			# Pie chart, where the slices will be ordered and plotted counter-clockwise:
			labels = 'CRYPTO', 'SP500', 'DJIA', 'NASDAQ'
			sizes = [50, 16.67, 16.67, 16.67]
			mycolors = ["yellow", "hotpink", "b", "#4CAF50"]
			explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
			fig1, ax1 = plt.subplots()
			ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
				shadow=True, startangle=90,colors = mycolors)
			ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

			st.pyplot(fig1)
		
				
		elif age>18 and age<=30:
			#print("allocate 50% of your portfolio to BTC")
			st.text("PORTFOLIO DESIGN AND RISK MANAGEMENT")
			st.text("allocate 50% of your portfolio to crypto and 50 % between the SP500,DJIA and NASDAQ indices")
			import streamlit as st
			import matplotlib.pyplot as plt
			#time.sleep(10)
			# Pie chart, where the slices will be ordered and plotted counter-clockwise:
			labels = 'CRYPTO', 'SP500', 'DJIA', 'NASDAQ'
			sizes = [50, 16.67, 16.67, 16.67]
			mycolors = ["yellow", "hotpink", "b", "#4CAF50"]
			explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
			fig1, ax1 = plt.subplots()
			ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
				shadow=True, startangle=90,colors = mycolors)
			ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

			st.pyplot(fig1)
			
		elif age>30 and age<=40:
			#print("allocate 40% of your portfolio to BTC")
			st.text("PORTFOLIO DESIGN AND RISK MANAGEMENT")
			st.text("allocate 40% of your portfolio to crypto and 60 % between the SP500,DJIA and NASDAQ indices")
			import streamlit as st
			import matplotlib.pyplot as plt
			#time.sleep(10)
			# Pie chart, where the slices will be ordered and plotted counter-clockwise:
			labels = 'CRYPTO', 'SP500', 'DJIA', 'NASDAQ'
			sizes = [40, 20, 20, 20]
			mycolors = ["yellow", "hotpink", "b", "#4CAF50"]
			explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
			fig1, ax1 = plt.subplots()
			ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
				shadow=True, startangle=90,colors = mycolors)
			ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

			st.pyplot(fig1)
			
		elif age>40 and age<=50:
			#print("allocate 30% of your portfolio to BTC")
			st.text("PORTFOLIO DESIGN AND RISK MANAGEMENT")
			st.text("allocate 30% of your portfolio to crypto and 70 % between the SP500,DJIA and NASDAQ indices")
			import streamlit as st
			import matplotlib.pyplot as plt
			#time.sleep(10)
			# Pie chart, where the slices will be ordered and plotted counter-clockwise:
			labels = 'CRYPTO', 'SP500', 'DJIA', 'NASDAQ'
			sizes = [30, 23.33, 23.33, 23.33]
			mycolors = ["yellow", "hotpink", "b", "#4CAF50"]
			explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
			fig1, ax1 = plt.subplots()
			ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
				shadow=True, startangle=90,colors = mycolors)
			ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

			st.pyplot(fig1)
			

		elif age>50 and age<=60:
			#print("allocate 20% of your portfolio to BTC")
			st.text("PORTFOLIO DESIGN AND RISK MANAGEMENT")
			st.text("allocate 20% of your portfolio to crypto and 80 % between the SP500,DJIA and NASDAQ indices")
			import streamlit as st
			import matplotlib.pyplot as plt
			#time.sleep(10)
			# Pie chart, where the slices will be ordered and plotted counter-clockwise:
			labels = 'CRYPTO', 'SP500', 'DJIA', 'NASDAQ'
			sizes = [20, 26.67, 26.67, 26.67]
			mycolors = ["yellow", "hotpink", "b", "#4CAF50"]
			explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
			fig1, ax1 = plt.subplots()
			ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
				shadow=True, startangle=90,colors = mycolors)
			ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

			st.pyplot(fig1)
			
			
		elif age>60 and age<=70:
			#print("allocate 10% of your portfolio to BTC")
			st.text("PORTFOLIO DESIGN AND RISK MANAGEMENT")
			st.text("allocate 10% of your portfolio to crypto and 90 % between the SP500,DJIA and NASDAQ indices")
			import streamlit as st
			import matplotlib.pyplot as plt
			#time.sleep(10)
			# Pie chart, where the slices will be ordered and plotted counter-clockwise:
			labels = 'CRYPTO', 'SP500', 'DJIA', 'NASDAQ'
			sizes = [10, 30, 30, 30]
			mycolors = ["yellow", "hotpink", "b", "#4CAF50"]
			explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
			fig1, ax1 = plt.subplots()
			ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
				shadow=True, startangle=90,colors = mycolors)
			ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

			st.pyplot(fig1)
			
			
		elif age>70 and age<=200:
			#print("allocate 5% of your portfolio to BTC")
			st.text("PORTFOLIO DESIGN AND RISK MANAGEMENT")
			st.text("allocate 5% of your portfolio to crypto and 95 % between the SP500,DJIA and NASDAQ indices")
			import streamlit as st
			import matplotlib.pyplot as plt
			#time.sleep(10)
			# Pie chart, where the slices will be ordered and plotted counter-clockwise:
			labels = 'CRYPTO', 'SP500', 'DJIA', 'NASDAQ'
			sizes = [5, 31.67, 31.67, 31.67]
			mycolors = ["yellow", "hotpink", "b", "#4CAF50"]
			explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
			fig1, ax1 = plt.subplots()
			ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
				shadow=True, startangle=90,colors = mycolors)
			ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
			st.pyplot(fig1)
			
			
		else:
			print("can not access the model.")
		crypto_portfolio()	
		
	with tab6:
		altcoinseason()
	with tab7:
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


		ax2.plot(df.Date, df.rsi,linewidth=0.5)
		st.set_option('deprecation.showPyplotGlobalUse', False)
		st.pyplot()
		#streamlit run momentum_strat.py
	with tab8:
		dca()	
	with tab9:
		import pandas as pd
		import numpy as np
		import streamlit as st

		import base64
		from io import BytesIO
		from matplotlib.backends.backend_pdf import FigureCanvasPdf as FigureCanvas

		#from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
		from matplotlib.figure import Figure



			#streamlit run downloading_report.py
		dataframe = pd.read_csv("satoshi 100 index data58.csv")
		#st.header("Top 100 Cryptocurrencies")
		st.header("Cryptocurrency Market Daily,Weekly and Monthly Report ")
		#data=pd.read_csv("satoshi 100 index data29.csv")
		#st.dataframe(dataframe)
		
		#print(df)
		i=0
		st.subheader("Today's Winners ")
		for i in range(10):
			
			data=dataframe.sort_values(by=['24H %'], ascending=False)
		st.dataframe(data)
		df = pd.DataFrame(data)

		if st.button("Download CSV1"):
			csv = df.to_csv(index=False)
			b64 = base64.b64encode(csv.encode()).decode()
			href = f'<a href="data:file/csv;base64,{b64}" download="mydata.csv">Download CSV File</a>'
			st.markdown(href, unsafe_allow_html=True)
		#csv_downloader()
		st.subheader("Today's Biggest Losers ")
		for i in range(10):
			
			data=dataframe.sort_values(by=['24H %'])
		st.dataframe(data)
		df = pd.DataFrame(data)

		if st.button("Download CSV2"):
			csv = df.to_csv(index=False)
			b64 = base64.b64encode(csv.encode()).decode()
			href = f'<a href="data:file/csv;base64,{b64}" download="mydata.csv">Download CSV File</a>'
			st.markdown(href, unsafe_allow_html=True)
		#csv_downloader()
		st.subheader("This week's Winners ")
		for i in range(10):
		
			data=dataframe.sort_values(by=['7D %'], ascending=False)
		st.dataframe(data)
		df = pd.DataFrame(data)

		if st.button("Download CSV3"):
			csv = df.to_csv(index=False)
			b64 = base64.b64encode(csv.encode()).decode()
			href = f'<a href="data:file/csv;base64,{b64}" download="mydata.csv">Download CSV File</a>'
			st.markdown(href, unsafe_allow_html=True)
		#csv_downloader()
		st.subheader("This week's Biggest lossers ")
		for i in range(10):
			
			data=dataframe.sort_values(by=['7D %'])
		st.dataframe(data)
		df = pd.DataFrame(data)

		if st.button("Download CSV4"):
			csv = df.to_csv(index=False)
			b64 = base64.b64encode(csv.encode()).decode()
			href = f'<a href="data:file/csv;base64,{b64}" download="mydata.csv">Download CSV File</a>'
			st.markdown(href, unsafe_allow_html=True)
		#csv_downloader()
		st.subheader("This Month's Winners ")
		for i in range(10):
			
			data=dataframe.sort_values(by=['30D %'], ascending=False)
		st.dataframe(data)
		df = pd.DataFrame(data)

		if st.button("Download CSV5"):
			csv = df.to_csv(index=False)
			b64 = base64.b64encode(csv.encode()).decode()
			href = f'<a href="data:file/csv;base64,{b64}" download="mydata.csv">Download CSV File</a>'
			st.markdown(href, unsafe_allow_html=True)
		#csv_downloader()
		st.subheader("This Month's Biggest Losers ")
		for i in range(10):
			
			data=dataframe.sort_values(by=['30D %'])
		st.dataframe(data)
		df = pd.DataFrame(data)

		if st.button("Download CSV6"):
			csv = df.to_csv(index=False)
			b64 = base64.b64encode(csv.encode()).decode()
			href = f'<a href="data:file/csv;base64,{b64}" download="mydata.csv">Download CSV File</a>'
			st.markdown(href, unsafe_allow_html=True)
		#csv_downloader()
		#streamlit run market_report.py
                
	with tab10:
		st.header("investor connect")
		st.text("share your charts below")
		uploaded_file = st.file_uploader("Choose a file")
		st.text("Coming Soon")
		st.image("bitcoin heatmap.png", width=800)
	with tab11:
		buy_crypto()
        
	
	
    
    
        
		
			
		

		
	#streamlit run cv.py
		

	#streamlit run finalc.py
#st.set_page_config(
 #   page_title="multipage app",
  #  page_icon="random",
    
#)
#st.title("main page")
#st.sidebar.success("select a page above")
#import streamlit as st



# Security
#passlib,hashlib,bcrypt,scrypt
import hashlib
def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False
# DB Management
import sqlite3 
conn = sqlite3.connect('data.db')
c = conn.cursor()
# DB  Functions
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data


def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data



def main():
	"""Simple Login App"""

	#st.title("Simple Login App")

	menu = ["Home","Login","SignUp","Logout","Reset Password"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		st.subheader("Home")
		st.write("Welcome to our platform!")
		topcryptos()
		#scrapping()
	elif choice == "Login":
		#st.subheader("Login Section")

		username = st.sidebar.text_input("User Name")
		password = st.sidebar.text_input("Password",type='password')
		if st.sidebar.checkbox("Login"):
			# if password == '12345':
			create_usertable()
			hashed_pswd = make_hashes(password)

			result = login_user(username,check_hashes(password,hashed_pswd))
			if result:

				st.success("Logged In as {}".format(username))

				#crypto_analytics()
				task = st.selectbox("Task",["Add Post","Analytics","Profiles"])
				if task == "Add Post":
					#st.subheader("Add Your Post")
					st.header("comments")
					comments = st.text_input('Leave a Comment Below: ')
					st.button('Submit Comment')

				elif task == "Analytics":
		
		            
					st.subheader("Analytics")
					crypto_analytics()
					
					
				elif task == "Profiles":
					st.subheader("User Profiles")
					user_result = view_all_users()
					clean_db = pd.DataFrame(user_result,columns=["Username","Password"])
					st.dataframe(clean_db)
			else:
				st.warning("Incorrect Username/Password")
	elif choice == "Logout":
            st.subheader("Logout Section")
            logout_button = st.button("Logout")
            if logout_button:
                st.sidebar.empty()
                st.warning("You have been logged out")
	elif choice == "Logout":
            st.subheader("Logout Section")
            logout_button = st.button("Logout")
            if logout_button:
                st.sidebar.empty()
                st.warning("You have been logged out")
	elif choice == "Reset Password":
		st.subheader("Reset Password")
		username = st.text_input("Username")
		old_password = st.text_input("Old Password", type='password')
		new_password = st.text_input("New Password", type='password')

		if st.button("Reset"):
			create_usertable()
			hashed_pswd = make_hashes(old_password)

			result = login_user(username, check_hashes(old_password, hashed_pswd))
			if result:
				reset_password(username, new_password)

			else:
				st.warning("Incorrect Username/Password")



	elif choice == "SignUp":
		st.subheader("Create New Account")
		new_user = st.text_input("Username")
		new_password = st.text_input("Password",type='password')

		if st.button("Signup"):
			create_usertable()
			add_userdata(new_user,make_hashes(new_password))
			st.success("You have successfully created a valid Account")
			st.info("Go to Login Menu to login")



if __name__ == '__main__':
	main()
#streamlit run streamlit_login.py
#streamlit run signup2.py