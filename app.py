import streamlit as st

# Title
st.title("My First Streamlit App")

# Text
st.write("Hello, Welcome to Streamlit 🚀")

# Input box
name = st.text_input("Enter your name")

# Button
if st.button("Submit"):
    st.success(f"Hello {name}, nice to meet you!")

# Slider
age = st.slider("Select your age", 0, 100, 18)
st.write("Your age is:", age)

# Checkbox
if st.checkbox("Show more info"):
    st.info("Streamlit makes web apps using only Python!")