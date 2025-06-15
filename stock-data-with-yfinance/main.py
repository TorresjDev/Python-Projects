import yfinance as yf
import pprint as pp
import plotly.express as px

# Stock Data with yfinance
# This script retrieves and visualizes stock data using the yfinance library.
# ***
# Jesus Torres
# ***
# Reference:
#  - yfinance Package: https://aroussi.com/post/python-yahoo-finance
#  - yfinance Documentation: https://ranaroussi.github.io/yfinance/index.html
#  - Plotly Express Documentation: https://plotly.com/python/plotly-express/
#

stock = yf.Ticker("AAPL")  # Retrieve stock information

apple_info = stock.info  # Get information about Apple Inc.

pp.pprint(dict(apple_info))

print(apple_info['longName'], ':',
      apple_info['sector'], ':', apple_info['industry'])

history_data = stock.history(period="5y")

fig = px.line(history_data, x=history_data.index, y=[
    'Open', 'High', 'Low', 'Close'], title='Apple Inc. Stock Prices', labels={
    'value': 'Stock Price (USD)', 'variable': 'Stock Price Type'})

fig.show(renderer='browser')

history_data.to_csv('apple_stock_5y_history.csv')
