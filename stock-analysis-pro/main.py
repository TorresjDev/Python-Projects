"""
Stock Analysis Pro - Main Application
Entry point that orchestrates the application with Stock and Crypto support
"""

import config
import stock_analyzer
import crypto_analyzer
import ui


def main():
    """Main application function"""
    # Initialize components
    config_manager = config.Config()
    stock_analyzer_instance = stock_analyzer.StockAnalyzer(config_manager)
    crypto_analyzer_instance = crypto_analyzer.CryptoAnalyzer(config_manager)
    user_interface = ui.UI(
        config_manager, stock_analyzer_instance, crypto_analyzer_instance)

    # Setup UI with Streamlit
    user_interface.setup_page()

    # Initialize session state for data persistence
    user_interface._initialize_session_state()

    # Header Container - Contains header and mode toggle
    user_interface.display_header()
    mode = user_interface.show_mode_toggle()

    if mode == "Stock":
        symbol, search_clicked = user_interface.show_stock_search()

        # Handle new stock search
        if symbol and search_clicked:
            if stock_analyzer_instance.validate_stock_symbol(symbol):
                with user_interface.show_loading(f"📊 Analyzing {symbol}..."):
                    hist_data, stock_info = stock_analyzer_instance.get_stock_data(
                        symbol, period="1y")

                    if hist_data is not None and stock_info:
                        # Store in session state
                        user_interface.store_stock_data(
                            hist_data, stock_info, symbol)
                    else:
                        user_interface.show_error(
                            "❌ Unable to fetch stock data. Please try again.")
            else:
                user_interface.show_validation_error(symbol)

        # Stock Data Container - Contains all stock analysis components
        if user_interface.has_stock_data():
            hist_data, stock_info, current_symbol = user_interface.get_stored_stock_data()

            with user_interface.create_data_container():
                # Display all stock analysis components
                user_interface.display_real_time_indicator()
                user_interface.display_stock_overview(
                    current_symbol, stock_info, hist_data)
                user_interface.display_stock_charts(
                    current_symbol, hist_data, "1y")
                user_interface.display_financial_metrics(stock_info, hist_data)
                user_interface.display_performance_metrics(hist_data)
                user_interface.display_company_info(stock_info)
                user_interface.display_description(stock_info)

    else:  # Crypto mode
        symbol, search_clicked = user_interface.show_crypto_search()

        # Handle new crypto search
        if symbol and search_clicked:
            if crypto_analyzer_instance.validate_crypto_symbol(symbol):
                with user_interface.show_loading(f"💹 Analyzing {symbol}..."):
                    crypto_data = crypto_analyzer_instance.get_crypto_data(
                        symbol)
                    hist_data = crypto_analyzer_instance.get_crypto_historical_data(
                        symbol)

                    if crypto_data:
                        # Store in session state
                        user_interface.store_crypto_data(
                            crypto_data, hist_data, symbol)
                    else:
                        user_interface.show_error(
                            "❌ Unable to fetch crypto data. Please try again.")
            else:
                user_interface.show_validation_error(symbol)

        # Crypto Data Container - Contains all crypto analysis components
        if user_interface.has_crypto_data():
            crypto_data, hist_data, current_symbol = user_interface.get_stored_crypto_data()

            with user_interface.create_data_container():
                # Display all crypto analysis components
                user_interface.display_real_time_indicator()
                user_interface.display_crypto_overview(
                    current_symbol, crypto_data)
                user_interface.display_crypto_charts(current_symbol, hist_data)
                user_interface.display_crypto_metrics(crypto_data)
                user_interface.display_crypto_performance(crypto_data)
                user_interface.display_crypto_info(crypto_data)


# Run the app
if __name__ == "__main__":
    main()
