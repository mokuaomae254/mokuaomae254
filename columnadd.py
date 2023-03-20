# importing pandas as pd
import pandas as pd
import streamlit as st

# Making data frame from the csv file
dataframe = pd.read_csv("nba.csv")

# Printing the first 10 rows of
# the data frame for visualization
#dataframe[:10]
# increase the salary by 10 %
data=dataframe.assign(Revised_Salary = lambda x: dataframe['Salary']
							+ dataframe['Salary']/10)
st.dataframe(data)
#streamlit run columnadd.py
