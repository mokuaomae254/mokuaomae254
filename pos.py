import streamlit as st

def position_sizing_calculator(account_size:float, risk_tolerance:float, entry_price:float, stop_loss:float):
    # Calculate the risk per trade
    risk_per_trade = (entry_price - stop_loss) * (risk_tolerance/100)
    # Calculate the position size
    position_size = account_size / risk_per_trade
    return position_size

# Get the user's account size
st.sidebar.subheader("Position Sizing Calculator")
account_size = st.sidebar.number_input("Enter your account size:", min_value=0, step=1)

# Get the user's risk tolerance
risk_tolerance = st.sidebar.slider("Risk Tolerance (as percentage of account)", min_value=1, max_value=20, step=1, value=5)

# Get the user's entry price
entry_price = st.sidebar.number_input("Enter the entry price:", min_value=0, step=0.01)

# Get the user's stop loss
stop_loss = st.sidebar.number_input("Enter the stop loss price:", min_value=0, step=0.01)

# Calculate the position size
position_size = position_sizing_calculator(account_size, risk_tolerance, entry_price, stop_loss)

# Print the position size
st.write("Position size: ", position_size)
#streamlit run pos.py