# Python website with Streamlit Project-9

import streamlit as st

# Title and Header
st.title("👋 Welcome to my Python Website!")
st.header("🚀 Explore some Amazing Features.")

# Adding some text
st.write("This is a simple Streamlit app built in just 15 minutes!")

# Adding a button
if st.button("👉 Click me"):
    st.write("Thank you for clicking the button! 😊")

# Adding user input
name = st.text_input("What is your name?").upper()
if st.button("🎉 Streamlit"):
    st.write(f"👋 Hello {name}! 🎈 Welcome to the Website!")
