import pandas as pd
import streamlit as st

### Data Import ###
dfMF = pd.read_csv("./Mutual funds Performance Tracker Nov 23.csv")

### INTRODUCTION ###
st.set_page_config(layout="wide")
st.title("Welcome to DP's Mutual funds Performance Tracker!")
st.subheader('Data as of 16-Nov-2023')

### Sidebar SELECTION ###
oneY = st.slider('Select returns for 1Y', 0, 100, 10)
threeY = st.slider('Select returns for 3Y', 0, 100, 10)

### Helper Methods ###

### Main Page content ###
st.dataframe(dfMF) # Same as st.write(dfMF)