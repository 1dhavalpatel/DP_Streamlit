import pandas as pd
import streamlit as st

st.title("Welcome to DP's Mutual funds Performance Tracker!")

dfMF = pd.read_csv('Mutual funds Performance Tracker Nov 23.csv')