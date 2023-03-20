"""
    
    
import streamlit as st
import pandas as pd
import base64
from io import BytesIO
from matplotlib.backends.backend_pdf import FigureCanvasPdf as FigureCanvas

#from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

def main():
    st.title("PDF Downloader")

    df = pd.DataFrame({'A':[1,2,3], 'B':[4,5,6]})

    st.write("Original Dataframe")
    st.dataframe(df)

    if st.button("Download PDF"):
        # Create a figure and axis
        #fig = Figure()
        #ax = fig.add_subplot()

        # Plot the dataframe
        #df.plot(kind='bar', ax=ax)

        # Customize the plot
        #ax.set_title("My Dataframe")

        # Convert the plot to a bytes object
        #buffer = BytesIO()
        #FigureCanvas(fig).print_pdf(buffer)
        #pdf_bytes = buffer.getvalue()
        #buffer.close()

        # Encode the bytes object as a base64 string
        b64 = base64.b64encode(pdf_bytes).decode()

        # Create a link to download the pdf
        href = f'<a href="data:application/pdf;base64,{b64}" download="mydata.pdf">Download PDF File</a>'
        st.markdown(href, unsafe_allow_html=True)

if __name__ == '__main__':
    main()

"""
""" 
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
    st.dataframe(df)

    if st.button("Download CSV"):
        csv = df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="mydata.csv">Download CSV File</a>'
        st.markdown(href, unsafe_allow_html=True)


if __name__ == '__main__':
    main()
"""
"""
import streamlit as st
import pandas as pd

import base64
from io import BytesIO
from matplotlib.backends.backend_pdf import FigureCanvasPdf as FigureCanvas

#from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
def main():
    st.title("PDF Downloader")
    #st.header("Top 100 Cryptocurrencies")
    data=pd.read_csv("satoshi 100 index data26.csv")
    #st.dataframe(data)

    
    df = pd.DataFrame(data)

    st.write("Original Dataframe")
    st.dataframe(df)

    if st.button("Download PDF"):
        pdf = df.to_pdf()
        b64 = base64.b64encode(pdf.encode()).decode()
        href = f'<a href="data:file/pdf;base64,{b64}" download="mydata.pdf">Download PDF File</a>'
        st.markdown(href, unsafe_allow_html=True)
if __name__ == '__main__':
    main()        
"""

import streamlit as st
import pandas as pd
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

def main():
    st.title("PDF Downloader")
    data=pd.read_csv("satoshi 100 index data26.csv")
    df = pd.DataFrame(data)

    st.write("Original Dataframe")
    st.dataframe(df)

    if st.button("Download PDF"):
        pdf_buffer = BytesIO()
        doc = SimpleDocTemplate(pdf_buffer, pagesize=landscape(letter))
        table = Table(df.values)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, -1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        doc.build([table])
        pdf_data = pdf_buffer.getvalue()
        pdf_buffer.seek(0)
        b64 = base64.b64encode(pdf_data).decode()
        href = f'<a href="data:application/pdf;base64,{b64}" download="mydata.pdf">Download PDF File</a>'
        st.markdown(href, unsafe_allow_html=True)

if __name__ == '__main__':
    main()