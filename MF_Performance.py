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
    st.markdown('Select the filters you want to apply')
    plan_radio = st.radio(
        "Choose the plan",("Regular", "Direct Plan"))
    sixM = st.slider('Select returns for 6M', 0, 100, 10)
    oneY = st.slider('Select returns for 1Y', 0, 100, 10)
    threeY = st.slider('Select returns for 3Y', 0, 100, 10)
    fiveY = st.slider('Select returns for 5Y', 0, 100, 10)
    tenY = st.slider('Select returns for 10Y', 0, 100, 10)

    
### Apply filters ###
dfMF = dfMF[dfMF['Plan'] == plan_radio]
dfMF = dfMF[dfMF['6M'] >= sixM]
dfMF = dfMF[dfMF['1Y'] >= oneY]
dfMF = dfMF[dfMF['3Y'] >= threeY]
dfMF = dfMF[dfMF['5Y'] >= fiveY]
dfMF = dfMF[dfMF['10Y'] >= tenY]

### Helper Methods ###

### Main Page content ###
col1, col2, col3 = st.columns(3)

with col1:
   st.header("Average AuM(Cr)")
   st.write(dfMF['AuM (Cr)'].mean().round(2))

with col2:
   st.header("Average 1Y return")
   st.write(dfMF['1Y'].mean().round(2))

with col3:
   st.header("Average 5Y return")
   st.write(dfMF['5Y'].mean().round(2))

st.dataframe(dfMF[['Scheme Name','Crisil Rank','AuM (Cr)','3M','6M','1Y','2Y','3Y','5Y','10Y']]) # Same as st.write(dfMF)