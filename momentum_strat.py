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
ax2.axhline(90, color="red",linewidth=0.8)
#ax2.axhline(50, color="black",linewidth=0.8)
ax2.axhline(20, color="green",linewidth=0.8)
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