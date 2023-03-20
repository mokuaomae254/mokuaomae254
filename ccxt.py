import streamlit as st
import ccxt
import talib

# Initialize exchange object
exchange = ccxt.binance({
    'rateLimit': 3000,
    'enableRateLimit': True,
})

# Set trading pair and timeframe
symbol = 'BTC/USDT'
timeframe = '1d'

# Fetch historical OHLCV data
ohlcv = exchange.fetch_ohlcv(symbol, timeframe)

# Calculate RSI
rsi = talib.RSI(ohlcv['close'], timeperiod=14)

# DCA parameters
dca_in_threshold = st.sidebar.slider('DCA In Threshold', 0, 100, 20)
dca_out_threshold = st.sidebar.slider('DCA Out Threshold', 0, 100, 80)
dca_amount = st.sidebar.number_input('DCA Amount (USD)', min_value=0, value=1000)

# Initialize variables
dca_active = False
dca_buy_price = 0

if st.button('Execute DCA'):
    for i in range(len(ohlcv['timestamp'])):
        if not dca_active:
            # Check if RSI is below dca_in_threshold
            if rsi[i] < dca_in_threshold:
                # Place a buy order
                dca_buy_price = exchange.create_market_buy_order(symbol, dca_amount/ohlcv['close'][i])
                dca_active = True
                st.success(f'DCA buy order placed at {dca_buy_price}')
        else:
            # Check if RSI is above dca_out_threshold
            if rsi[i] > dca_out_threshold:
                # Place a sell order
                sell_price = exchange.create_market_sell_order(symbol, dca_amount/dca_buy_price)
                dca_active = False
                st.success(f'DCA sell order placed at {sell_price}')
else:
    st.warning('Please press the execute button to run the script')

#