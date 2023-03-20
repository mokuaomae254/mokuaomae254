#import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
age=int(input("enter your age:"))
if age<18:
    print("your are not of age to invest")
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
elif age in range(18,30):
     print("hello2")
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
elif age in range(30,40):
    print("hello2")
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
elif age in range(40,50):
    print("hello3")
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
elif age in range(50,60):
    print("hello4")
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
elif age in range(60,70):
    print("hello5")
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
elif age in range(70,150):
    print("hello6")
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
else:
    print("cannot access the model")
    

    
         
    
    
    
    
#switch_caseimplementation.py