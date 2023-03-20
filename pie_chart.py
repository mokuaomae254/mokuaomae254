import streamlit as st
import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'CRYPTO', 'SP500', 'DJIA', 'NASDAQ'
sizes = [50, 16.67, 16.67, 16.67]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot(fig1)
#streamlit run pie_chart.py

""""#figsize=(20,10)
#st.pyplot(fig1size=(2,1))
#streamlit run pie_chart.py
#With Pyplot, you can use the pie() function to draw pie charts:
#Start the first wedge at 90 degrees:
plt.pie(y, labels = mylabels, startangle = 90)
#Maybe you want one of the wedges to stand out? The explode parameter allows you to do that.
plt.pie(y, labels = mylabels, explode = myexplode)
#Add a shadow to the pie chart by setting the shadows parameter to True:
plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)
#You can set the color of each wedge with the colors parameter.
mycolors = ["black", "hotpink", "b", "#4CAF50"]

plt.pie(y, labels = mylabels, colors = mycolors)
'r' - Red
'g' - Green
'b' - Blue
'c' - Cyan
'm' - Magenta
'y' - Yellow
'k' - Black
'w' - White
#To add a list of explanation for each wedge, use the legend() function:
plt.pie(y, labels = mylabels)
plt.legend()
#To add a header to the legend, add the title parameter to the legend function.
plt.legend(title = "Four Fruits:")
""""
