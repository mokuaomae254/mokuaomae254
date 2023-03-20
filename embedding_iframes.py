
import streamlit as st
#iframe_tag = '<iframe src="https://www.example.com" width="800" height="600"></iframe>'

iframe_tag = '<iframe src='https://tradingeconomics.com/embed/?s=cpi+yoy&v=202212131344v20220312&h=300&w=600&ref=/united-states/inflation-cpi' height='300' width='600'  frameborder='0' scrolling='no'></iframe>'<br />source: <a href='https://tradingeconomics.com/united-states/inflation-cpi'>tradingeconomics.com</a>

st.markdown(iframe_tag, unsafe_allow_html=True)


#streamlit run embedding_iframes.py