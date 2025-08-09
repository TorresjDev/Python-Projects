from datetime import date, datetime
import time
import streamlit as st
import yfinance as yf

# Display a styled title in HTML format
st.header("Stock Price App.")
st.subheader("Jesus Torres")
st.write("""
    Reference:
    - Streamlit Framework: https://streamlit.io
    - Streamlit Documentation: https://docs.streamlit.io/library/api-reference
    - yfinance Package: https://aroussi.com/post/python-yahoo-finance
    - yfinance Documentation: https://ranaroussi.github.io/yfinance/index.html
    """)

# Brief description of the app's purpose
st.write("This app retrieves stock data from Yahoo Finance API and displays it in a user-friendly format.")


# Create a dropdown menu for selecting a stock
stock_name = st.selectbox('Select a stock to check', options=stock_list)

# Input for selecting the start date of stock data, default is January 1, 2024
start_date = st.date_input('Start Date', datetime(2024, 1, 1))
# Input for selecting the end date of stock data, default is today
end_date = st.date_input("End Date")

# Store today's date for validation
today = date.today()


def stream_summary(summary: str):
    """
    Function to stream the business summary of the stock.
    This function takes a summary string and yields each word with a slight delay
    """
    for word in summary.split(" "):
        yield word + " "
        time.sleep(0.02)  # Simulate a delay for streaming effect


# Action to retrieve stock data when the 'Submit' button is clicked
if st.button('Submit'):
    # Check if selected dates are valid (not in the future)
    if (start_date > today) or (end_date > today) or (start_date > end_date):
        st.warning("Please select a valid date period.")
    else:
        # Get data for the selected stock from yfinance API
        stock = yf.Ticker(stock_name)

        # Get stock information
        stock_info = stock.get_info()

        # Retrieve historical data between selected dates
        stock_history = stock.history(start=start_date, end=end_date)

        # Display Stock information
        st.header(
            f"****Stock Name: {stock_info['longName']}**** ({stock_info['symbol']})")
        st.subheader(f" **Sector:** {stock_info['sector']}")
        st.subheader(f"**Industry:** {stock_info['industry']}")
        # Display stock business summary using write_stream for better formatting
        st.subheader("Business Summary:")
        st.write_stream(stream_summary(stock_info['longBusinessSummary']))

        st.write("**Raw Data of Stock Price**")
        # Display raw data of stock price
        st.dataframe(stock_history)
        # Plot stock price data (Open, High, Low, Close)
        st.line_chart(stock_history, y=['Open', 'High', 'Low', 'Close'])

        # Display a success message upon completion
        st.success('Done')
