# Importing the streamlit library to create web applications easily
import streamlit as st

# This creates a large heading at the top of the app
st.title ("My First Dashboard App")
# This displays a welcome message on the top
st.write("Hello, welcome to my First Dashboard app!")

user_input = st.text_input ("Enter your name")
# The st.text_input() function creates a text box where the user can type their name
# The text entered by the user is stored in the variable 'user_input'

st.write(f"Congratulations, {user_input} ! this is your first dashboard")
# The st.write() function dynamically updates to greet the user by name.