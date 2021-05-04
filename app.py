import yfinance as yf
import streamlit as st

st.write("""
# Simple Stock Price App
Shown are the stock *closing price* and volume of Tesla!
""")



tickerSymbol = 'TSLA'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d', start='2015-1-1', end='2021-4-30')

st.write("""
# Closing price""")
st.line_chart(tickerDf.Close)

st.write("""
# Volume price""")
st.line_chart(tickerDf.Volume)