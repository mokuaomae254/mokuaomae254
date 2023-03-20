

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


# Initialize variables to keep track of investment
investment_count = 0
total_invested = 0
shares_bought = 0

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
final_value = shares_bought * row["Value"]
st.write("Total invested: ${}".format(total_invested))
st.write("Final value of investment: {:.2f}".format(final_value))


#streamlit run dca_strat.py
"""
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

  
    

"""