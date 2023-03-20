import streamlit as st
import yfinance as yf

st.title("AAPL Stock Price")

# Get AAPL stock data
aapl = yf.Ticker("AAPL")
hist = aapl.history(period="1mo")

# Display stock data in Streamlit app
st.write(hist.tail())

#streamlit run yfinance.py