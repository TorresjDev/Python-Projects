"""
Stock Analyzer class
Handles stock analysis logic and data processing

"""

import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta
import requests


class StockAnalyzer:
    """Stock analyzer for data processing and analysis logic"""

    def __init__(self, config):
        """Initialize analyzer with configuration"""
        self.config = config
        self.cache = {}
        self.cache_expiry = {}

    def validate_stock_symbol(self, symbol):
        """Validate if a stock symbol exists"""
        try:
            if not symbol or len(symbol.strip()) == 0:
                return False
            stock = yf.Ticker(symbol)
            info = stock.info
            if info and (info.get('regularMarketPrice') or info.get('currentPrice') or
                         info.get('previousClose') or info.get('longName')):
                return True
            return False
        except:
            return False

    def get_stock_data(self, symbol, period="1y"):
        """Fetch stock data with caching"""
        try:
            cache_key = f"{symbol}_{period}"
            if self._is_cache_valid(cache_key):
                return self.cache[cache_key]

            stock = yf.Ticker(symbol)
            hist = stock.history(period=period)
            info = stock.info

            self._cache_data(cache_key, (hist, info))
            return hist, info
        except Exception:
            return None, None

    def calculate_price_change(self, current_price, previous_price):
        """Calculate price change and percentage"""
        if previous_price == 0:
            return 0, 0
        change = current_price - previous_price
        pct_change = (change / previous_price) * 100
        return change, pct_change

    def create_price_chart(self, data, symbol, period):
        """Create interactive price chart"""
        if data is None or data.empty:
            return None
        print(f"Creating price chart for {symbol} with period {period}")
        print(f"Data: {data}")
        fig = go.Figure()
        fig.add_trace(go.Candlestick(
            x=data.index,
            open=data['Open'],
            high=data['High'],
            low=data['Low'],
            close=data['Close'],
            name=symbol,
            increasing_line_color=self.config.chart_settings['colors']['positive'],
            decreasing_line_color=self.config.chart_settings['colors']['negative'],
            increasing_fillcolor="rgba(16, 185, 129, 0.3)",
            decreasing_fillcolor="rgba(239, 68, 68, 0.3)"
        ))

        fig.update_layout(
            title=f'{symbol} Stock Price',
            yaxis_title='Price (USD)',
            xaxis_title='Date',
            template=self.config.chart_settings['theme'],
            height=500,
            showlegend=False,
            margin=dict(l=50, r=50, t=50, b=50)
        )
        fig.update_xaxes(rangeslider_visible=False)
        return fig

    def create_volume_chart(self, data, symbol):
        """Create volume chart"""
        if data is None or data.empty:
            return None

        fig = go.Figure()
        colors = [self.config.chart_settings['colors']['positive'] if close >= open_price
                  else self.config.chart_settings['colors']['negative']
                  for close, open_price in zip(data['Close'], data['Open'])]

        fig.add_trace(go.Bar(
            x=data.index,
            y=data['Volume'],
            marker_color=colors,
            name='Volume',
            opacity=0.7
        ))

        fig.update_layout(
            title=f'{symbol} Trading Volume',
            yaxis_title='Volume',
            xaxis_title='Date',
            template=self.config.chart_settings['theme'],
            height=200,
            showlegend=False,
            margin=dict(l=50, r=50, t=30, b=30)
        )
        return fig

    def format_large_number(self, num):
        """Format large numbers"""
        if num >= 1e12:
            return f"${num/1e12:.1f}T"
        elif num >= 1e9:
            return f"${num/1e9:.1f}B"
        elif num >= 1e6:
            return f"${num/1e6:.1f}M"
        elif num >= 1e3:
            return f"${num/1e3:.1f}K"
        else:
            return f"${num:.2f}"

    def get_financial_metrics(self, stock_info, hist_data):
        """Get formatted financial metrics"""
        volume = hist_data['Volume'].iloc[-1] if not hist_data.empty else 0
        avg_volume = hist_data['Volume'].rolling(
            window=20).mean().iloc[-1] if len(hist_data) >= 20 else volume

        print(f"stock_info: {stock_info}")
        print(f"hist_data: {hist_data}")

        return {
            "Market Cap": self.format_large_number(stock_info.get('marketCap', 0)) if stock_info.get('marketCap') else "N/A",
            "P/E Ratio": f"{stock_info.get('trailingPE', 0):.2f}" if isinstance(stock_info.get('trailingPE'), (int, float)) else "N/A",
            "Volume": f"{volume:,.0f}",
            "Avg Volume (20d)": f"{avg_volume:,.0f}",
            "52W High": f"${stock_info.get('fiftyTwoWeekHigh', 'N/A')}",
            "52W Low": f"${stock_info.get('fiftyTwoWeekLow', 'N/A')}",
            "Beta": f"{stock_info.get('beta', 'N/A')}",
            "Dividend Yield": f"{stock_info.get('dividendYield', 0):.2f}%" if stock_info.get('dividendYield') else "N/A"}

    def get_company_info(self, stock_info):
        """Get formatted company information"""
        return {
            "Industry": stock_info.get('industry', 'N/A'),
            "Sector": stock_info.get('sector', 'N/A'),
            "Employees": f"{stock_info.get('fullTimeEmployees', 0):,}" if stock_info.get('fullTimeEmployees') else "N/A",
            "Founded": stock_info.get('foundationYear', 'N/A'),
            "Headquarters": f"{stock_info.get('city', '')}, {stock_info.get('country', '')}" if stock_info.get('city') else 'N/A',
            "Website": stock_info.get('website', 'N/A')
        }

    def calculate_performance_metrics(self, hist_data):
        """Calculate performance metrics"""
        if len(hist_data) == 0:
            return {}

        perf_periods = {"1 Day": 1, "1 Week": 5,
                        "1 Month": 20, "3 Months": 60, "1 Year": 252}
        performance = {}

        for period_name, days in perf_periods.items():
            if len(hist_data) > days:
                start_price = hist_data['Close'].iloc[-days-1]
                end_price = hist_data['Close'].iloc[-1]
                perf_change = ((end_price - start_price) / start_price) * 100
                color = "🟢" if perf_change > 0 else "🔴" if perf_change < 0 else "🟡"
                performance[f"{color} {period_name}"] = f"{perf_change:+.2f}%"
        return performance

    def _is_cache_valid(self, cache_key):
        """Check if cached data is valid"""
        if cache_key not in self.cache or cache_key not in self.cache_expiry:
            return False
        return datetime.now() < self.cache_expiry[cache_key]

    def _cache_data(self, cache_key, data):
        """Cache data with expiry"""
        self.cache[cache_key] = data
        self.cache_expiry[cache_key] = datetime.now(
        ) + timedelta(minutes=self.config.cache_settings['expiry_minutes'])
