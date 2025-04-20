import streamlit as st

# Title for the website
st.title('Simple Python Website with Streamlit')

# Description
st.write("""
This is a simple Streamlit app where you can enter your name, and I'll greet you!
""")

# User input: name
name = st.text_input('Enter your name:')

# Button to show the result
if st.button('Submit'):
    if name:
        st.write(f'Hello, {name}! Welcome to the Streamlit app!')
    else:
        st.write('Please enter a name.')

# Adding a simple plot (optional)
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.title('Simple Plot')
st.pyplot(plt)

