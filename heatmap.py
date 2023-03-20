
"""
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
"""

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
#streamlit run heatmap.py