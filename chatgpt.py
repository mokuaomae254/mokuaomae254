import streamlit as st
import pandas as pd
import hashlib

def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password, hashed_text):
    if make_hashes(password) == hashed_text:
        return hashed_text
    return False

import sqlite3
conn = sqlite3.connect('data.db')
c = conn.cursor()

def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT, password TEXT)')

def add_userdata(username, password):
    c.execute('INSERT INTO userstable(username, password) VALUES (?, ?)', (username, password))
    conn.commit()

def login_user(username, password):
    c.execute('SELECT * FROM userstable WHERE username = ? AND password = ?', (username, password))
    data = c.fetchall()
    return data

def view_all_users():
    c.execute('SELECT * FROM userstable')
    data = c.fetchall()
    return data

def main():
    """Simple Login App"""
    import streamlit as st
    import pandas as pd
    import numpy as np
    import time
    import matplotlib
    import matplotlib.pyplot as plt
    matplotlib.use('TkAgg')

    st.title("Simple Login App")

    menu = ["Home", "Login", "SignUp"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")

    elif choice == "Login":
        st.subheader("Login Section")

        username = st.sidebar.text_input("User Name")
        password = st.sidebar.text_input("Password", type='password')
        if st.sidebar.checkbox("Login"):
            create_usertable()
            hashed_pswd = make_hashes(password)

            result = login_user(username, check_hashes(password, hashed_pswd))
            if result:
                st.success("Logged In as {}".format(username))

                task = st.selectbox("Task", ["Add Post", "Analytics", "Profiles"])
                if task == "Add Post":
                    st.subheader("Add Your Post")

                elif task == "Analytics":
                    st.subheader("Analytics")

                    st.set_page_config(layout="wide")
                    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs(["RISK DISCLAIMER", "Top 100 Cryptocurrencies", "Macro Analysis", "Sentiment Analysis", "portfolio design and risk management", "Altcoin Season Index", "Onchain Analysis", "investor connect", "comments"])
                    with tab1:
                        st.header("RISK DISCLAIMER")

                        st.text(" \n\r       Before
import talib
import pandas as pd

def rsi_trading_strategy(data, rsi_periods, buy_threshold, sell_threshold):
    # Calculate RSI values
    rsi = talib.RSI(data['Close'], rsi_periods)
    
    # Initialize empty list of signals
    signals = []
    
    # Loop through RSI values and determine buy/sell signals
    for i in range(len(rsi)):
        if rsi[i] < buy_threshold:
            signals.append('BUY')
        elif rsi[i] > sell_threshold:
            signals.append('SELL')
        else:
            signals.append('HOLD')
    
    return signals

# Load historical data
data = pd.read_csv('data.csv')

# Test trading strategy
signals = rsi_trading_strategy(data, 14, 30, 70)
print(signals)

import streamlit as st

def position_sizing(price, risk_tolerance, stop_loss):
    # Calculate risk per trade as a percentage of account balance
    risk_per_trade = risk_tolerance / 100
    
    # Calculate position size
    position_size = risk_per_trade / (stop_loss * price)
    
    # Round position size to nearest whole number
    position_size = round(position_size)
    
    return position_size

def main():
    # Create input fields for market price, risk tolerance, and stop-loss
    price = st.number_input('Market Price')
    risk_tolerance = st.number_input('Risk Tolerance (% of account balance)')
    stop_loss = st.number_input('Stop-Loss (percentage of market price)')
    
    # Add button to trigger position sizing calculation
    if st.button('Calculate Position Size'):
        # Calculate and display position size
        position_size = position_sizing(price, risk_tolerance, stop_loss)
        st.write(f'Position size: {position_size}')

if __name__ == '__main__':
    main()
