"""
Crypto Analyzer class
Handles cryptocurrency analysis logic and data processing using CoinMarketCap API
"""

import requests
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta


class CryptoAnalyzer:
    """Crypto analyzer for data processing and analysis logic"""

    def __init__(self, config):
        """Initialize analyzer with configuration"""
        self.config = config
        self.cache = {}
        self.cache_expiry = {}
        self.api_key = config.api_keys.get('coinmarketcap')
        self.base_url = "https://pro-api.coinmarketcap.com/v1"

    def validate_crypto_symbol(self, symbol):
        """Validate if a crypto symbol exists"""
        try:
            if not symbol or len(symbol.strip()) == 0:
                return False

            if not self.api_key:
                return False

            url = f"{self.base_url}/cryptocurrency/quotes/latest"
            headers = {"X-CMC_PRO_API_KEY": self.api_key}
            params = {"symbol": symbol.upper()}

            response = requests.get(
                url, headers=headers, params=params, timeout=10)
            if response.status_code == 200:
                data = response.json()
                return symbol.upper() in data.get("data", {})
            return False
        except Exception:
            return False

    def get_crypto_data(self, symbol):
        """Fetch crypto data with caching"""
        try:
            cache_key = f"crypto_{symbol.upper()}"
            if self._is_cache_valid(cache_key):
                return self.cache[cache_key]

            if not self.api_key:
                return None

            url = f"{self.base_url}/cryptocurrency/quotes/latest"
            headers = {"X-CMC_PRO_API_KEY": self.api_key}
            params = {"symbol": symbol.upper()}

            response = requests.get(
                url, headers=headers, params=params, timeout=10)
            if response.status_code == 200:
                data = response.json()
                crypto_data = data["data"][symbol.upper()]

                self._cache_data(cache_key, crypto_data)
                return crypto_data
            return None
        except Exception:
            return None

    def get_crypto_historical_data(self, symbol, days=365):
        """Get historical crypto data (Note: CoinMarketCap free tier has limited historical data)"""
        # For now, return mock historical data since CoinMarketCap historical requires paid tier
        # In a real implementation, you might use other APIs like CoinGecko for free historical data
        try:
            current_data = self.get_crypto_data(symbol)
            if not current_data:
                return None

            current_price = current_data["quote"]["USD"]["price"]

            # Generate mock historical data for demonstration
            dates = pd.date_range(end=datetime.now(), periods=days, freq='D')
            prices = []
            base_price = current_price

            for i in range(days):
                # Add some realistic price variation
                variation = (hash(f"{symbol}_{i}") %
                             200 - 100) / 1000  # -10% to +10% variation
                price = base_price * \
                    (1 + variation * (i / days))  # Gradual trend
                prices.append(max(price, 0.01))  # Ensure positive prices

            hist_data = pd.DataFrame({
                'Date': dates,
                'Close': prices,
                'Open': [p * 0.995 for p in prices],  # Mock open prices
                'High': [p * 1.02 for p in prices],   # Mock high prices
                'Low': [p * 0.98 for p in prices],    # Mock low prices
                'Volume': [1000000 + (hash(f"{symbol}_{i}_vol") % 5000000) for i in range(days)]
            })
            hist_data.set_index('Date', inplace=True)

            return hist_data
        except Exception:
            return None

    def calculate_price_change(self, current_price, previous_price):
        """Calculate price change and percentage"""
        if previous_price == 0:
            return 0, 0
        change = current_price - previous_price
        pct_change = (change / previous_price) * 100
        return change, pct_change

    def create_crypto_price_chart(self, hist_data, symbol):
        """Create interactive crypto price chart"""
        if hist_data is None or hist_data.empty:
            return None

        fig = go.Figure()
        fig.add_trace(go.Candlestick(
            x=hist_data.index,
            open=hist_data['Open'],
            high=hist_data['High'],
            low=hist_data['Low'],
            close=hist_data['Close'],
            name=symbol,
            increasing_line_color=self.config.chart_settings['colors']['positive'],
            decreasing_line_color=self.config.chart_settings['colors']['negative'],
            increasing_fillcolor="rgba(16, 185, 129, 0.3)",
            decreasing_fillcolor="rgba(239, 68, 68, 0.3)"
        ))

        fig.update_layout(
            title=f'{symbol} Crypto Price',
            yaxis_title='Price (USD)',
            xaxis_title='Date',
            template=self.config.chart_settings['theme'],
            height=500,
            showlegend=False,
            margin=dict(l=50, r=50, t=50, b=50)
        )
        fig.update_xaxes(rangeslider_visible=False)
        return fig

    def create_crypto_volume_chart(self, hist_data, symbol):
        """Create crypto volume chart"""
        if hist_data is None or hist_data.empty:
            return None

        fig = go.Figure()
        colors = [self.config.chart_settings['colors']['positive'] if close >= open_price
                  else self.config.chart_settings['colors']['negative']
                  for close, open_price in zip(hist_data['Close'], hist_data['Open'])]

        fig.add_trace(go.Bar(
            x=hist_data.index,
            y=hist_data['Volume'],
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
        """Format large numbers for crypto (similar to stock analyzer)"""
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

    def get_crypto_metrics(self, crypto_data):
        """Get formatted crypto metrics"""
        try:
            quote_data = crypto_data["quote"]["USD"]

            return {
                "Market Cap": self.format_large_number(quote_data.get("market_cap", 0)),
                "Volume (24h)": self.format_large_number(quote_data.get("volume_24h", 0)),
                "Volume Change (24h)": f"{quote_data.get('volume_change_24h', 0):.2f}%",
                "Price Change (1h)": f"{quote_data.get('percent_change_1h', 0):.2f}%",
                "Price Change (24h)": f"{quote_data.get('percent_change_24h', 0):.2f}%",
                "Price Change (7d)": f"{quote_data.get('percent_change_7d', 0):.2f}%",
                "Price Change (30d)": f"{quote_data.get('percent_change_30d', 0):.2f}%",
                "Circulating Supply": f"{crypto_data.get('circulating_supply', 0):,.0f}",
            }
        except Exception:
            return {"Error": "Unable to fetch crypto metrics"}

    def get_crypto_info(self, crypto_data):
        """Get formatted crypto information"""
        try:
            return {
                "Name": crypto_data.get("name", "N/A"),
                "Symbol": crypto_data.get("symbol", "N/A"),
                "Rank": crypto_data.get("cmc_rank", "N/A"),
                "Max Supply": f"{crypto_data.get('max_supply', 0):,.0f}" if crypto_data.get('max_supply') else "N/A",
                "Total Supply": f"{crypto_data.get('total_supply', 0):,.0f}" if crypto_data.get('total_supply') else "N/A",
                "Date Added": crypto_data.get("date_added", "N/A")[:10] if crypto_data.get("date_added") else "N/A",
                "Tags": ", ".join(crypto_data.get("tags", [])[:3]) if crypto_data.get("tags") else "N/A"
            }
        except Exception:
            return {"Error": "Unable to fetch crypto info"}

    def calculate_crypto_performance(self, crypto_data):
        """Calculate crypto performance metrics from API data"""
        try:
            quote_data = crypto_data["quote"]["USD"]
            performance = {}

            # Get performance data directly from API
            periods = {
                "🔴 1 Hour": quote_data.get("percent_change_1h", 0),
                "🔴 24 Hours": quote_data.get("percent_change_24h", 0),
                "🔴 7 Days": quote_data.get("percent_change_7d", 0),
                "🔴 30 Days": quote_data.get("percent_change_30d", 0),
                "🔴 60 Days": quote_data.get("percent_change_60d", 0),
                "🔴 90 Days": quote_data.get("percent_change_90d", 0)
            }

            for period_name, change in periods.items():
                if change is not None:
                    color = "🟢" if change > 0 else "🔴" if change < 0 else "🟡"
                    clean_period = period_name.replace("🔴 ", "")
                    performance[f"{color} {clean_period}"] = f"{change:+.2f}%"

            return performance
        except Exception:
            return {"Error": "Unable to calculate performance"}

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
