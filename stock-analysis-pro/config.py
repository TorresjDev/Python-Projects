"""
Configuration file
Handles environment setup and API configuration

"""

import os
from dotenv import load_dotenv


class Config:
    """Configuration class"""

    def __init__(self):
        """Constructor method for initializing the Config class"""
        self.api_keys = {}
        self.app_settings = {}
        self.chart_settings = {}
        self.cache_settings = {}

        # Auto-load environment on initialization
        self.load_environment()

    def load_environment(self):
        """Load environment variables from .env file"""
        try:
            load_dotenv()

            # API Keys
            # self.api_keys = {
            #     'coinmarketcap': os.getenv("COINMARKETCAP_API_KEY"),
            #     'google': os.getenv("GOOGLE_API_KEY")
            # }

            # Application Settings
            self.app_settings = {
                'title': os.getenv("APP_TITLE", "Stock Analysis Pro"),
                'author': os.getenv("APP_AUTHOR", "Jesus Torres"),
                'default_refresh_interval': int(os.getenv("DEFAULT_REFRESH_INTERVAL", 10)),
                'default_stock_symbol': os.getenv("DEFAULT_STOCK_SYMBOL", "TSLA"),
            }

            # Chart Settings
            self.chart_settings = {
                'theme': os.getenv("DEFAULT_CHART_THEME", "plotly_white"),
                'default_period': os.getenv("DEFAULT_TIME_PERIOD", "1y"),
                'colors': {
                    'positive': '#10b981',
                    'negative': '#ef4444',
                    'neutral': '#6b7280',
                    'primary': '#3b82f6',
                    'background': '#f8fafc'
                },
                'time_periods': {
                    "1D": "1d", "1W": "5d", "1M": "1mo",
                    "3M": "3mo", "6M": "6mo", "1Y": "1y", "5Y": "5y"
                }
            }

            # Cache Settings
            self.cache_settings = {
                'expiry_minutes': int(os.getenv("CACHE_EXPIRY_MINUTES", 5)),
                'max_size_mb': int(os.getenv("MAX_CACHE_SIZE_MB", 100))
            }

            return True, "Environment loaded successfully"

        except Exception as e:
            return False, f"Error loading environment: {str(e)}"

    def validate_config(self):
        """Validate configuration settings"""
        warnings = []

        if not self.api_keys.get('coinmarketcap'):
            warnings.append(
                "COINMARKETCAP_API_KEY not found - crypto features will be disabled")

      #   if not self.api_keys.get('google'):
      #       warnings.append(
      #           "GOOGLE_API_KEY not found - AI features will be disabled")

        return warnings
