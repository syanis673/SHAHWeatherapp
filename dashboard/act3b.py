import streamlit as st
import pandas as pd

st.title("Fecth and Display Data from a URL")

# Fecth data
url = 'https://storage.dosm.gov.my/population/population_state.csv'
url_data = pd.read_csv(url)

# Display data
st.subheader("Display Data from URL")
st.dataframe(url_data, use_container_width=True)
st.caption("Displaying data fecthed from an online source")