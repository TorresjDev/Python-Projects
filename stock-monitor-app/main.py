import yfinance as yf
import streamlit as st
import requests
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Access the API key
COINMARKETCAP_API_KEY = os.getenv("COINMARKETCAP_API_KEY")

# Check if the API key is available
if not COINMARKETCAP_API_KEY:
    st.error("API Key for CoinMarketCap is missing! Please check your .env file.")

# Set the title of the app
st.title("Stock & Crypto Monitor")

# Layout with columns
col1, col2 = st.columns(2)

# Stock Data in Column 1
with col1:
    st.header("📈 Stock Data", divider=True)
    stock_ticker = st.text_input("Enter Stock Ticker (e.g., AAPL, TSLA):", "AAPL", key="stock")
    date_range = st.selectbox("Select Date Range:", ["1mo", "3mo", "6mo", "1y", "5y"])
    if stock_ticker:
        stock_data = yf.Ticker(stock_ticker)
        stock_df = stock_data.history(period=date_range)
        st.line_chart(stock_df["Close"])

# Crypto Data in Column 2
with col2:
    st.header("💹 Crypto Data", divider=True)
    crypto_symbol = st.text_input("Enter Crypto Symbol (e.g., BTC, ETH):", "BTC", key="crypto")
    if crypto_symbol:
        api_url = f"https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
        headers = {"X-CMC_PRO_API_KEY": COINMARKETCAP_API_KEY}
        params = {"symbol": crypto_symbol}

        response = requests.get(api_url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            crypto_data = data["data"][crypto_symbol]["quote"]["USD"]
            print(crypto_data)
            price = crypto_data["price"]
            market_cap = crypto_data["market_cap"]
            volume_24h = crypto_data["volume_24h"]

            st.write(f"Price: ${price:.2f}")
            st.write(f"Market Cap: ${market_cap:,.2f}")
            st.write(f"24h Volume: ${volume_24h:,.2f}")
        else:
            st.error("Failed to fetch crypto data. Check the symbol or API key.")
