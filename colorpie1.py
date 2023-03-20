import streamlit as st
import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'BITCOIN', 'SP500', 'DJIA', 'NASDAQ'
sizes = [50, 16.67, 16.67, 16.67]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot(fig1)
#streamlit run colorpie1.py