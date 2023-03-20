import pandas as pd
import numpy as np
import streamlit as st

import base64
from io import BytesIO
from matplotlib.backends.backend_pdf import FigureCanvasPdf as FigureCanvas

#from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure



    #streamlit run downloading_report.py
dataframe = pd.read_csv("satoshi 100 index data58.csv")
#dataframe = pd.read_csv("satoshi 100 index data31.csv")
#st.header("Top 100 Cryptocurrencies")
st.header("Cryptocurrency Market Daily,Weekly and Monthly Report ")
#data=pd.read_csv("satoshi 100 index data29.csv")
#st.dataframe(dataframe)
   
#print(df)
i=0
st.subheader("Today's Winners ")
for i in range(10):
    
    data=dataframe.sort_values(by=['24H %'], ascending=False)
st.dataframe(data)
df = pd.DataFrame(data)

if st.button("Download CSV1"):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="mydata.csv">Download CSV File</a>'
    st.markdown(href, unsafe_allow_html=True)
#csv_downloader()
st.subheader("Today's Biggest Losers ")
for i in range(10):
    
    data=dataframe.sort_values(by=['24H %'])
st.dataframe(data)
df = pd.DataFrame(data)

if st.button("Download CSV2"):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="mydata.csv">Download CSV File</a>'
    st.markdown(href, unsafe_allow_html=True)
#csv_downloader()
st.subheader("This week's Winners ")
for i in range(10):
   
    data=dataframe.sort_values(by=['7D %'], ascending=False)
st.dataframe(data)
df = pd.DataFrame(data)

if st.button("Download CSV3"):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="mydata.csv">Download CSV File</a>'
    st.markdown(href, unsafe_allow_html=True)
#csv_downloader()
st.subheader("This week's Biggest lossers ")
for i in range(10):
    
    data=dataframe.sort_values(by=['7D %'])
st.dataframe(data)
df = pd.DataFrame(data)

if st.button("Download CSV4"):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="mydata.csv">Download CSV File</a>'
    st.markdown(href, unsafe_allow_html=True)
#csv_downloader()
st.subheader("This Month's Winners ")
for i in range(10):
    
    data=dataframe.sort_values(by=['30D %'], ascending=False)
st.dataframe(data)
df = pd.DataFrame(data)

if st.button("Download CSV5"):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="mydata.csv">Download CSV File</a>'
    st.markdown(href, unsafe_allow_html=True)
#csv_downloader()
st.subheader("This Month's Biggest Losers ")
for i in range(10):
    
    data=dataframe.sort_values(by=['30D %'])
st.dataframe(data)
df = pd.DataFrame(data)

if st.button("Download CSV6"):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="mydata.csv">Download CSV File</a>'
    st.markdown(href, unsafe_allow_html=True)
#csv_downloader()
#streamlit run market_report.py