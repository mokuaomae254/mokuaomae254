import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.title("Altcoin Season Indicator")

# Read in dataframe
dataframe = pd.read_csv("satoshi 100 index data28.csv")

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
        # Create a new column that calculates the percentage difference between each coin's 24H % and Bitcoin BTC's 24H %
        top_99["Difference"] = top_99["24H %"] - bitcoin_24H_perc.values[0]

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

#streamlit run last.py