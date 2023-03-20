import streamlit as st
import pandas as pd

# load your dataset
data = pd.read_csv('btc_prices.csv')

# set your trading parameters (e.g. amount of bitcoin to buy, percentage dip to trigger buy)
buy_amount = 0.1
dip_percentage = 3

# create a variable to store the current price
current_price = None

st.header('Buy the Dip Bitcoin Trading Strategy')

# create a line chart to visualize the data
st.line_chart(data)

# create a function to check if the price has dipped
def check_dip(new_price):
    global current_price
    if current_price is None:
        current_price = new_price
        return False
    else:
        price_change = 100 * (new_price - current_price) / current_price
        if price_change <= -dip_percentage:
            current_price = new_price
            return True
        else:
            current_price = new_price
            return False

# create a button to manually check for a dip
if st.button('Check for Dip'):
    # get the latest closing price
    latest_price = data['close'].iloc[-1]
    if check_dip(latest_price):
        st.success(f'Dip detected! Bought {buy_amount} BTC at {latest_price}')
    else:
        st.info(f'No dip detected. Current price: {latest_price}')



#Add a new column to the dataframe that calculates the 20 day MA:
data['20d_MA'] = data['close'].rolling(window=20).mean()
#Modify the check_dip() function to also check if the current price is below the 20 day MA:
def check_dip(new_price):
    global current_price
    if current_price is None:
        current_price = new_price
        return False
    else:
        price_change = 100 * (new_price - current_price) / current_price
        if price_change <= -dip_percentage and new_price < data['20d_MA'].iloc[-1]:
            current_price = new_price
            return True
        else:
            current_price = new_price
            return False

#Add a line chart to visualize the 20d MA with the data
st.line_chart(data[['close','20d_MA']])
#This will now check if the current price is below the 20 day MA in addition to checking if the price has dipped by the specified percentage before triggering a buy signal.
Please note that this is a very basic example and does not include any risk management or stop loss strategy. It is important to have a well-defined trading strategy and risk management plan before executing any trades. Also, it is not recommended to use a single moving average as a trading strategy, it's important to consider multiple indicators, volatility and to diversify your portfolio.

