import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.title("World! Welcome to Streamlit!")

fig = plt.figure(figsize=(16,9), dpi=400)
plt.bar(dfFinNumbers.Month, dfFinNumbers.GrossExpense, color= 'orange', label="Gross Expense")
plt.bar(dfFinNumbers.Month, dfFinNumbers.GrossIncome, color= 'green', label="Gross Income")
plt.plot(dfFinNumbers.Month, dfFinNumbers.NetIncome, color= 'blue', label="Net Income", marker='*')

plt.title('KHH Numbers in Lakh', y=1.05, fontsize=18, color='blue')

# calling the function to add value labels
#addlabels(dfFinNumbers.RptMonth, dfFinNumbers.NetIncome)

plt.legend()
st.pyplot(fig)