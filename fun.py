import talib as ta
import math
import streamlit as st

def ma(source, length, type):
    if type == "SMA":
        return ta.sma(source, length)
    elif type == "Bollinger Bands":
        return ta.sma(source, length)
    elif type == "EMA":
        return ta.ema(source, length)
    elif type == "SMMA (RMA)":
        return ta.sma(source, length)
    elif type == "WMA":
        return ta.wma(source, length)
    elif type == "VWMA":
        return ta.vwma(source, length)

st.title("Relative Strength Index")

rsi_settings = st.sidebar.selectbox("RSI Settings", ["RSI Length", "Source"], index=0)
if rsi_settings == "RSI Length":
    rsiLengthInput = st.sidebar.number_input("RSI Length", min_value=1, value=14)
elif rsi_settings == "Source":
    rsiSourceInput = st.sidebar.selectbox("Source", ["close"], index=0)

ma_settings = st.sidebar.selectbox("MA Settings", ["MA Type", "MA Length", "BB StdDev"], index=0)
if ma_settings == "MA Type":
    maTypeInput = st.sidebar.selectbox("MA Type", ["SMA", "Bollinger Bands", "EMA", "SMMA (RMA)", "WMA", "VWMA"], index=0)
elif ma_settings == "MA Length":
    maLengthInput = st.sidebar.number_input("MA Length", min_value=1, value=14)
elif ma_settings == "BB StdDev":
    bbMultInput = st.sidebar.number_input("BB StdDev", min_value=0.001, max_value=50, value=2.0)
up = ta.SMA(max(ta.ROC(eval(rsiSourceInput)), 0), rsiLengthInput)
down = ta.SMA(-max(ta.ROC(eval(rsiSourceInput)), 0), rsiLengthInput)

rsi = 100 - (100 / (1 + up / down)) if down != 0 else 0 if up != 0 else 100
rsiMA = ma(rsi, maLengthInput, maTypeInput)
isBB = maTypeInput == "Bollinger Bands"

st.line_chart(rsi, "RSI", color='#7E57C2')
st.line_chart(rsiMA, "RSI-based MA", color='yellow')
st.hline(70, "RSI Upper Band", color='#787B86')
st.hline(50, "RSI Middle Band", color='#787B86')
st.hline(30, "RSI Lower Band", color='#787B86')
bbUpperBand = rsiMA + ta.stdev(rsi, maLengthInput) * bbMultInput if isBB else None
bbLowerBand = rsiMA - ta.stdev(rsi, maLengthInput) * bbMultInput if isBB else None
if isBB:
    st.fill_between(bbUpperBand, bbLowerBand, "Bollinger Bands Background Fill", color='green')


#streamlit run fun.py