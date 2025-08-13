"""
UI components
Handles all Streamlit interface components
"""

import streamlit as st
from datetime import datetime


class UI:
    """UI class for all interface components"""

    def __init__(self, config, stock_analyzer, crypto_analyzer):
        """Initialize UI with config and analyzers"""
        self.config = config
        self.stock_analyzer = stock_analyzer
        self.crypto_analyzer = crypto_analyzer

    def setup_page(self):
        """Configure Streamlit page"""
        st.set_page_config(
            page_title="Stock Analysis Pro",
            page_icon="📈",
            layout="wide",
            initial_sidebar_state="collapsed"
        )
        self._inject_custom_css()
        self._initialize_session_state()

    def _initialize_session_state(self):
        """Initialize session state variables"""
        if 'stock_data' not in st.session_state:
            st.session_state.stock_data = None
        if 'current_symbol' not in st.session_state:
            st.session_state.current_symbol = None
        if 'crypto_data' not in st.session_state:
            st.session_state.crypto_data = None
        if 'crypto_symbol_stored' not in st.session_state:
            st.session_state.crypto_symbol_stored = None
        if 'analysis_mode' not in st.session_state:
            st.session_state.analysis_mode = "Stock"

    def create_header_container(self):
        """Create and return the header container"""
        return st.container(width="stretch", border=True)

    def create_data_container(self):
        """Create and return the data container (unified for stock and crypto)"""
        return st.container(width="stretch", border=True)

    def store_stock_data(self, hist_data, stock_info, symbol):
        """Store stock data in session state"""
        st.session_state.stock_data = (hist_data, stock_info)
        st.session_state.current_symbol = symbol

    def get_stored_stock_data(self):
        """Get stored stock data from session state"""
        if st.session_state.stock_data is not None and st.session_state.current_symbol:
            hist_data, stock_info = st.session_state.stock_data
            current_symbol = st.session_state.current_symbol
            return hist_data, stock_info, current_symbol
        return None, None, None

    def has_stock_data(self):
        """Check if stock data exists in session state"""
        return st.session_state.stock_data is not None and st.session_state.current_symbol

    def store_crypto_data(self, crypto_data, hist_data, symbol):
        """Store crypto data in session state"""
        st.session_state.crypto_data = (crypto_data, hist_data)
        st.session_state.crypto_symbol_stored = symbol

    def get_stored_crypto_data(self):
        """Get stored crypto data from session state"""
        if st.session_state.crypto_data is not None and st.session_state.get('crypto_symbol_stored'):
            crypto_data, hist_data = st.session_state.crypto_data
            current_symbol = st.session_state.crypto_symbol_stored
            return crypto_data, hist_data, current_symbol
        return None, None, None

    def has_crypto_data(self):
        """Check if crypto data exists in session state"""
        return st.session_state.crypto_data is not None and st.session_state.get('crypto_symbol_stored')

    def display_header(self):
        """Display application header"""
        col1, col2, col3 = st.columns([1, 4, 1])
        with col2:
            st.markdown("""
            <div style='text-align: center'>
                <h1 style='color: #daa520; margin-bottom: -10px;'>
                    📈 Stock Analysis Pro
                </h1>
                <p style='color: #a0a0a0; font-size: 18px;'>
                    Professional Stock & Crypto Analysis • Real-time Data
                </p>
            </div>
            """, unsafe_allow_html=True)

    def show_mode_toggle(self):
        """Display mode toggle for Stock vs Crypto"""
        col1, col2, col3 = st.columns([1, 3, 1])
        with col2:
            st.markdown("""
                <div style='text-align: center; margin: 20px 0 10px 0;'>
                    <h3 style='color: #666; margin-bottom: 15px;'>Analysis Mode</h3>
                </div>
                """, unsafe_allow_html=True)

            # Create a centered container for the toggle
            st.markdown("""
                <div style='text-align: center; margin-bottom: 10px;'>
                    <span style='font-size: 18px; font-weight: 500;'>
                        Toggle between Stock & Crypto Analysis
                    </span>
                </div>
            """, unsafe_allow_html=True)

            # Centered toggle below label
            toggle_col1, toggle_col2, toggle_col3 = st.columns(
                [6, 3, 4], gap="medium", width="stretch")
            with toggle_col2:
                # Get current mode from session state
                current_mode = st.session_state.get('analysis_mode', 'Stock')

                is_crypto = st.toggle(
                    label="",
                    # value=current_mode == 'Crypto',
                    help="Toggle between Stock and Crypto analysis",
                    key="analysis_mode_toggle"
                )

                # Update mode based on toggle state
                if is_crypto:
                    new_mode = "Crypto"
                    st.session_state.previous_mode = current_mode == "Crypto"
                    st.write("🪙 Crypto")
                else:
                    new_mode = "Stock"
                    st.session_state.previous_mode = current_mode == "Stock"
                    st.write("Stock")

                # Update session state only if mode actually changed
                if st.session_state.analysis_mode != new_mode:
                    st.session_state.analysis_mode = new_mode

                return new_mode

    def display_real_time_indicator(self):
        """Display real-time update indicator"""
        current_time = datetime.now().strftime("%H:%M:%S")
        st.markdown(f"""
        <div style='text-align: center; color: #4CAF50; font-size: 14px; margin: 10px 0;'>
            🔴 Live • Last updated: {current_time} • Updates every 10 seconds
        </div>
        """, unsafe_allow_html=True)

    def display_stock_overview(self, symbol, stock_info, hist_data):
        """Display stock overview section"""
        if stock_info:
            current_price = stock_info.get(
                'currentPrice') or stock_info.get('regularMarketPrice', 0)
            prev_close = stock_info.get('previousClose', current_price)
            change, pct_change = self.stock_analyzer.calculate_price_change(
                current_price, prev_close)

            color = "#4CAF50" if change >= 0 else "#f44336"
            arrow = "↗" if change >= 0 else "↘"

            # Responsive column layout
            col1, col2 = st.columns([1, 1], gap="medium")

            with col1:
                st.markdown(f"""
                <div style='display: flex; justify-content: center;'>
                    <div class='stock-card' style='height: 120px; width: 100%; max-width: 300px; display: flex; flex-direction: column; justify-content: center; text-align: center; box-sizing: border-box; padding: 4.5rem 0px;'>
                        <h2 style='color: #333; margin: 0;'>{stock_info.get('longName', symbol)}</h2>
                        <h3 style='color: #666; margin: 0; font-size: 16px;'>{symbol}</h3>
                    </div>
                </div>
                """, unsafe_allow_html=True)

            with col2:
                st.markdown(f"""
                <div style='display: flex; justify-content: center;'>
                    <div class='stock-card' style='height: 120px; width: 100%; max-width: 300px; display: flex; flex-direction: column; justify-content: center; text-align: right; box-sizing: border-box; padding: 4rem 0px;'>
                        <h1 style='color: #333; margin: 0;'>${current_price:.2f}</h1>
                        <h3 style='color: {color}; margin: 0;'>
                            {arrow} ${change:.2f} ({pct_change:+.2f}%)
                        </h3>
                    </div>
                </div>
                """, unsafe_allow_html=True)

    def display_stock_charts(self, symbol, hist_data, period):
        """Display price and volume charts for stocks"""

        st.markdown("""
            <div style='text-align: center'>
                <h2 style='color: #daa520; '>
                    📊 Price Analysis
                </h2>
            </div>
            """, unsafe_allow_html=True)

      # Centered Chart period selector
        st.markdown("""
         <div style='text-align: center; margin: 1rem 0 0 0;'>
               <h4 style='color: #666;'>📅 Time Period</h4>
         </div>
         """, unsafe_allow_html=True)

      # Center the selectbox
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            selected_period = st.selectbox(
                "Time Period",
                ["1MO", "3MO", "6MO", "1Y", "2Y", "5Y", "10Y", "YTD", "MAX"],
                index=3,
                key="chart_period",
                label_visibility="collapsed"  # Hide the label since we show it above
            )

        # If period changed, fetch new data for the charts
        if selected_period != period:
            with st.spinner(f"📊 Loading {selected_period} data..."):
                new_hist_data, _ = self.stock_analyzer.get_stock_data(
                    symbol, period=selected_period.lower())
                if new_hist_data is not None:
                    hist_data = new_hist_data

        # Price chart
        price_chart = self.stock_analyzer.create_price_chart(
            hist_data, symbol, selected_period)
        if price_chart:
            st.plotly_chart(price_chart, use_container_width=True)

        # Volume chart
        volume_chart = self.stock_analyzer.create_volume_chart(
            hist_data, symbol)
        if volume_chart:
            st.plotly_chart(volume_chart, use_container_width=True)

    def display_financial_metrics(self, stock_info, hist_data):
        """Display financial metrics for stocks"""
        st.markdown("### 💰 Financial Metrics")

        metrics = self.stock_analyzer.get_financial_metrics(
            stock_info, hist_data)

        col1, col2, col3, col4 = st.columns(4)
        metric_items = list(metrics.items())

        for i, (key, value) in enumerate(metric_items):
            col = [col1, col2, col3, col4][i % 4]
            with col:
                st.metric(key, value)

    def display_performance_metrics(self, hist_data):
        """Display performance metrics for stocks"""
        st.markdown("### 📈 Performance")

        performance = self.stock_analyzer.calculate_performance_metrics(
            hist_data)

        if performance:
            cols = st.columns(len(performance))
            for i, (period, perf) in enumerate(performance.items()):
                with cols[i]:
                    st.metric(period, perf)

    def display_company_info(self, stock_info):
        """Display company information"""
        st.markdown("### 🏢 Company Information")

        company_info = self.stock_analyzer.get_company_info(stock_info)

        col1, col2 = st.columns(2)

        with col1:
            for key, value in list(company_info.items())[:3]:
                st.write(f"**{key}:** {value}")

        with col2:
            for key, value in list(company_info.items())[3:]:
                st.write(f"**{key}:** {value}")

    def display_description(self, stock_info):
        """Display company description"""
        description = stock_info.get('longBusinessSummary')
        if description:
            st.markdown("### 📋 Business Summary")
            st.write(description)

    def show_stock_search(self):
        """Display stock search interface"""
        with st.container():
            col1, col2, col3 = st.columns(
                [4, 2, 4], gap="medium", vertical_alignment="bottom")
            with col2:
                # Centered Search Stock header
                st.markdown("""
                     <div style='text-align: center'>
                        <h3>
                           🔍 Search Stock
                        </h3>
                     </div>
                     """, unsafe_allow_html=True)

                symbol = st.text_input(
                    "Enter stock symbol",
                    placeholder="e.g., NVDA, MSFT, TSLA, AAPL",
                    max_chars=10,
                    key="stock_symbol",
                    width=500
                ).upper().strip()

                # Search button
                search_clicked = st.button(
                    "🔍 Analyze Stock",
                    use_container_width=True,
                    type="secondary"
                )

                return symbol, search_clicked

    def show_crypto_search(self):
        """Display crypto search interface"""
        with st.container():
            col1, col2, col3 = st.columns(
                [4, 2, 4], gap="medium", vertical_alignment="bottom")
            with col2:
                # Centered Search Crypto header
                st.markdown("""
                     <div style='text-align: center'>
                        <h3>
                           🔍 Search Crypto
                        </h3>
                     </div>
                     """, unsafe_allow_html=True)

                symbol = st.text_input(
                    "Enter crypto symbol",
                    placeholder="e.g., BTC, ETH, ADA, SOL",
                    max_chars=10,
                    key="crypto_symbol_input",
                    width=500
                )

                # Handle empty input case
                if symbol:
                    symbol = symbol.upper().strip()
                else:
                    symbol = ""

                # Search button
                search_clicked = st.button(
                    "💹 Analyze Crypto",
                    use_container_width=True,
                    type="secondary"
                )

                return symbol, search_clicked

    def display_crypto_overview(self, symbol, crypto_data):
        """Display crypto overview section"""
        try:
            quote_data = crypto_data["quote"]["USD"]
            current_price = quote_data.get("price", 0)
            price_change_24h = quote_data.get("percent_change_24h", 0)
            price_change_abs = current_price * (price_change_24h / 100)

            color = "#4CAF50" if price_change_24h >= 0 else "#f44336"
            arrow = "↗" if price_change_24h >= 0 else "↘"

            # Responsive column layout
            col1, col2 = st.columns([1, 1], gap="medium")

            with col1:
                st.markdown(f"""
                <div style='display: flex; justify-content: center;'>
                    <div class='stock-card' style='height: 120px; width: 100%; max-width: 330px; display: flex; flex-direction: column; justify-content: center; text-align: center; box-sizing: border-box; padding: 7rem 0rem;'>
                        <h2 style='color: #333; margin: 0;'>{crypto_data.get('name', symbol)}</h2>
                        #{crypto_data.get('cmc_rank', 'N/A')}</h3>
                        <h3 style='color: #666; margin: 0; font-size: 16px;'>{symbol}
                    </div>
                </div>
                """, unsafe_allow_html=True)

            with col2:
                st.markdown(f"""
                <div style='display: flex; justify-content: center;'>
                    <div class='stock-card' style='height: 120px; width: 100%; max-width: 330px; display: flex; flex-direction: column; justify-content: center; text-align: right; box-sizing: border-box; padding: 7rem 0rem;'>
                        <h1 style='color: #333; margin: 0;'>${current_price:.4f}</h1>
                        <h3 style='color: {color}; margin: 0;'>
                            {arrow} ${price_change_abs:.4f} ({price_change_24h:+.2f}%)
                        </h3>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        except Exception:
            st.error("Unable to display crypto overview")

    def display_crypto_charts(self, symbol, hist_data):
        """Display crypto charts"""
        st.markdown("""
            <div style='text-align: center'>
                <h2 style='color: #daa520; '>
                    💹 Price Analysis
                </h2>
            </div>
            """, unsafe_allow_html=True)

        # Centered Chart period selector (similar to stock charts)
        st.markdown("""
         <div style='text-align: center; margin: 1rem 0 0 0;'>
               <h4 style='color: #666;'>📅 Time Period</h4>
         </div>
         """, unsafe_allow_html=True)

        # Center the selectbox
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            selected_period = st.selectbox(
                "Time Period",
                ["1MO", "3MO", "6MO", "1Y", "2Y"],
                index=3,  # Default to 1Y
                key="crypto_chart_period",
                label_visibility="collapsed"  # Hide the label since we show it above
            )

        # Map period selection to days for crypto data
        period_days = {
            "1MO": 30,
            "3MO": 90,
            "6MO": 180,
            "1Y": 365,
            "2Y": 730
        }

        # If period changed or hist_data is None, fetch new data
        selected_days = period_days.get(selected_period, 365)
        if hist_data is None or len(hist_data) != selected_days:
            with st.spinner(f"💹 Loading {selected_period} crypto data..."):
                hist_data = self.crypto_analyzer.get_crypto_historical_data(
                    symbol, days=selected_days)

        if hist_data is not None and not hist_data.empty:
            # Price chart
            price_chart = self.crypto_analyzer.create_crypto_price_chart(
                hist_data, symbol)
            if price_chart:
                st.plotly_chart(price_chart, use_container_width=True)

            # Volume chart
            volume_chart = self.crypto_analyzer.create_crypto_volume_chart(
                hist_data, symbol)
            if volume_chart:
                st.plotly_chart(volume_chart, use_container_width=True)
        else:
            st.info("📊 Historical crypto data visualization coming soon!")

    def display_crypto_metrics(self, crypto_data):
        """Display crypto metrics"""
        st.markdown("### 💰 Crypto Metrics")

        metrics = self.crypto_analyzer.get_crypto_metrics(crypto_data)

        col1, col2, col3, col4 = st.columns(4)
        metric_items = list(metrics.items())

        for i, (key, value) in enumerate(metric_items):
            col = [col1, col2, col3, col4][i % 4]
            with col:
                st.metric(key, value)

    def display_crypto_performance(self, crypto_data):
        """Display crypto performance metrics"""
        st.markdown("### 📈 Performance")

        performance = self.crypto_analyzer.calculate_crypto_performance(
            crypto_data)

        if performance:
            # Limit to 6 columns max
            cols = st.columns(min(len(performance), 6))
            for i, (period, perf) in enumerate(performance.items()):
                if i < 6:  # Display max 6 performance metrics
                    with cols[i]:
                        st.metric(period, perf)

    def display_crypto_info(self, crypto_data):
        """Display crypto information"""
        st.markdown("### 🪙 Cryptocurrency Information")

        crypto_info = self.crypto_analyzer.get_crypto_info(crypto_data)

        col1, col2 = st.columns(2)

        with col1:
            for key, value in list(crypto_info.items())[:4]:
                st.write(f"**{key}:** {value}")

        with col2:
            for key, value in list(crypto_info.items())[4:]:
                st.write(f"**{key}:** {value}")

    def show_loading(self, message="Loading..."):
        """Show loading indicator"""
        return st.spinner(message)

    def show_error(self, message):
        """Display error message"""
        st.error(message)

    def show_validation_error(self, symbol):
        """Show validation error message"""
        st.error(f"❌ **'{symbol}' is not a valid stock symbol**")
        st.info("💡 Try searching for: TSLA, MSFT, NVDA, AAPL")

    def _inject_custom_css(self):
        """Inject custom CSS for Robinhood-style appearance"""
        st.markdown("""
        <style>
        .main {
            padding-top: 2rem;
        }

        .stock-card {
            background: white;
            border-radius: 12px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            border-left: 4px solid #4CAF50;
            margin: 1rem 0;
        }

        .metric-card {
            background: #f8f9fa;
            padding: 1rem;
            border-radius: 8px;
            text-align: center;
            border: 1px solid #e9ecef;
        }

        .stSelectbox > div > div {
            border-radius: 8px;
        }

        .stTextInput > div > div > input {
            border-radius: 8px;
            border: 2px solid #e9ecef;
            padding: 0.75rem;
            font-size: 16px;
        }

        .stTextInput > div > div > input:focus {
            border-color: #4CAF50;
            box-shadow: 0 0 0 0.2rem rgba(76, 175, 80, 0.25);
        }

        div[data-testid="metric-container"] {
            background: white;
            border: 1px solid #e9ecef;
            padding: 1rem 0 0 0;
            border-radius: 8px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }
        </style>
        """, unsafe_allow_html=True)
