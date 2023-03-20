import matplotlib.pyplot as plt
import streamlit as st

# Data
x = [0, 1, 2, 3, 4, 5, 6]
y = [0, 1, 4, 9, 16, 25, 36]

# Plot
A = 6  # We want figures to be A6
plt.figure(figsize=(5,2))
plt.plot(x, y)
plt.title('This image is A6, dpi=100')
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()
#streamlit run resizing.py
