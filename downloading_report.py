import streamlit as st
import pandas as pd

import base64
from io import BytesIO
from matplotlib.backends.backend_pdf import FigureCanvasPdf as FigureCanvas

#from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
def main():
    st.title("CSV Downloader")
    #st.header("Top 100 Cryptocurrencies")
    data=pd.read_csv("satoshi 100 index data26.csv")
    #st.dataframe(data)
   

    df = pd.DataFrame(data)

    st.write("Original Dataframe")
    #st.dataframe(df)

    if st.button("Download CSV"):
        csv = df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="mydata.csv">Download CSV File</a>'
        st.markdown(href, unsafe_allow_html=True)


if __name__ == '__main__':
    main()

#streamlit run downloading_report.py