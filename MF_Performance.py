import pandas as pd
import streamlit as st

### Data Import ###
dfMF = pd.read_csv("./Mutual funds Performance Tracker Nov 23.csv")

### Data Cleanup ###
dfMF['1W'] = dfMF['1W'].str.replace('%', '').fillna(0).astype(float)
dfMF['1M'] = dfMF['1M'].str.replace('%', '').fillna(0).astype(float)
dfMF['3M'] = dfMF['3M'].str.replace('%', '').fillna(0).astype(float)
dfMF['6M'] = dfMF['6M'].str.replace('%', '').fillna(0).astype(float)
dfMF['1Y'] = dfMF['1Y'].str.replace('%', '').fillna(0).astype(float)
dfMF['2Y'] = dfMF['2Y'].str.replace('%', '').fillna(0).astype(float)
dfMF['3Y'] = dfMF['3Y'].str.replace('%', '').fillna(0).astype(float)
dfMF['5Y'] = dfMF['5Y'].str.replace('%', '').fillna(0).astype(float)
dfMF['10Y'] = dfMF['10Y'].str.replace('%', '').fillna(0).astype(float)

### INTRODUCTION ###
st.set_page_config(layout="wide")
st.title("Welcome to DP's Mutual funds Performance Tracker!")
st.subheader('Data as of 16-Nov-2023')

### Sidebar SELECTION ###
with st.sidebar:
    oneY = st.slider('Select returns for 1Y', 0, 100, 10)
    threeY = st.slider('Select returns for 3Y', 0, 100, 10)
    fiveY = st.slider('Select returns for 5Y', 0, 100, 10)
    tenY = st.slider('Select returns for 10Y', 0, 100, 10)

### Apply filters ###
dfMF = dfMF[dfMF['1Y'] >= oneY]
dfMF = dfMF[dfMF['3Y'] >= threeY]
dfMF = dfMF[dfMF['5Y'] >= fiveY]
dfMF = dfMF[dfMF['10Y'] >= tenY]

### Helper Methods ###

### Main Page content ###
st.dataframe(dfMF) # Same as st.write(dfMF)