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
                print(
                    f"Fetched crypto data for {symbol.upper()}: {crypto_data}")
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

            # Generate more realistic historical data for demonstration
            dates = pd.date_range(end=datetime.now(), periods=days, freq='D')

            # Create realistic price movements
            base_prices = []
            current_price_working = current_price

            # Work backwards from current price to create realistic historical trend
            for i in range(days):
                # Create daily volatility (crypto is more volatile than stocks)
                daily_change = (hash(f"{symbol}_{i}_daily") %
                                200 - 100) / 100  # -100% to +100%
                daily_volatility = daily_change * 0.05  # Scale to 5% max daily change

                # Add weekly trend
                weekly_trend = (hash(f"{symbol}_{i//7}_weekly") %
                                100 - 50) / 1000  # Weekly trend

                # Calculate price for this day
                price_change = daily_volatility + weekly_trend
                current_price_working *= (1 + price_change)
                current_price_working = max(
                    current_price_working, 0.001)  # Ensure positive

                base_prices.append(current_price_working)

            # Reverse to get chronological order
            base_prices.reverse()

            # Generate OHLC data from base prices
            ohlc_data = []
            for i, base_price in enumerate(base_prices):
                # Generate realistic OHLC from base price
                # 0-10% intraday range
                daily_volatility = (
                    hash(f"{symbol}_{i}_intraday") % 100) / 1000

                # Create open, high, low, close
                open_price = base_price * \
                    (1 + (hash(f"{symbol}_{i}_open") % 40 - 20) / 1000)
                close_price = base_price * \
                    (1 + (hash(f"{symbol}_{i}_close") % 40 - 20) / 1000)

                high_price = max(open_price, close_price) * \
                    (1 + daily_volatility)
                low_price = min(open_price, close_price) * \
                    (1 - daily_volatility)

                # Ensure logical OHLC relationship
                high_price = max(high_price, open_price, close_price)
                low_price = min(low_price, open_price, close_price)

                ohlc_data.append({
                    'Open': max(open_price, 0.001),
                    'High': max(high_price, 0.001),
                    'Low': max(low_price, 0.001),
                    'Close': max(close_price, 0.001),
                    # 1M-11M volume
                    'Volume': 1000000 + (hash(f"{symbol}_{i}_vol") % 10000000)
                })

            data = pd.DataFrame(ohlc_data, index=dates)
            return data

        except Exception as e:
            print(f"Error generating crypto historical data: {e}")
            return None

    def calculate_price_change(self, current_price, previous_price):
        """Calculate price change and percentage"""
        if previous_price == 0:
            return 0, 0
        change = current_price - previous_price
        pct_change = (change / previous_price) * 100
        return change, pct_change

    def create_crypto_price_chart(self, data, symbol):
        """Create interactive crypto price chart"""
        if data is None or data.empty:
            return None

        fig = go.Figure()

        # Create candlestick chart with proper colors
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
            decreasing_fillcolor="rgba(239, 68, 68, 0.3)",
            line=dict(width=1),
            increasing_line_width=1,
            decreasing_line_width=1
        ))

        fig.update_layout(
            title=f'{symbol} Crypto Price',
            yaxis_title='Price (USD)',
            xaxis_title='Date',
            template='plotly_white',
            height=500,
            showlegend=False,
            margin=dict(l=50, r=50, t=50, b=50),
        )

        # Remove range slider and configure x-axis
        fig.update_xaxes(
            rangeslider_visible=False,
            showgrid=True,
            gridwidth=1,
            gridcolor='rgba(128,128,128,0.2)'
        )

        # Configure y-axis
        fig.update_yaxes(
            showgrid=True,
            gridwidth=1,
            gridcolor='rgba(128,128,128,0.2)'
        )

        return fig

    def create_crypto_volume_chart(self, data, symbol):
        """Create crypto volume chart"""
        if data is None or data.empty:
            return None

        fig = go.Figure()

        # Create volume bars with colors based on price movement
        colors = [self.config.chart_settings['colors']['positive'] if close >= open_price
                  else self.config.chart_settings['colors']['negative']
                  for close, open_price in zip(data['Close'], data['Open'])]

        fig.add_trace(go.Bar(
            x=data.index,
            y=data['Volume'],
            marker_color=colors,
            name='Volume',
            opacity=0.7,
            marker_line_width=0
        ))

        fig.update_layout(
            title=f'{symbol} Trading Volume',
            yaxis_title='Volume',
            xaxis_title='Date',
            template='plotly_white',
            height=200,
            showlegend=False,
            margin=dict(l=50, r=50, t=30, b=30),

        )

        # Configure axes
        fig.update_xaxes(
            showgrid=True,
            gridwidth=1,
            gridcolor='rgba(128,128,128,0.2)'
        )

        fig.update_yaxes(
            showgrid=True,
            gridwidth=1,
            gridcolor='rgba(128,128,128,0.2)'
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
                "Market Dominance": f"{quote_data.get('market_cap_dominance', 0):.2f}%",
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
