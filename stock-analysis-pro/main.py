"""
Stock Analysis Pro - Main Application
Entry point that orchestrates the application
"""

from streamlit import user
import config
import stock_analyzer
import ui


def main():
    """Main application function"""
    # Initialize components
    config_manager = config.Config()
    analyzer = stock_analyzer.StockAnalyzer(config_manager)
    user_interface = ui.UI(config_manager, analyzer)

    # Setup UI with Streamlit
    user_interface.setup_page()

    # Initialize session state for stock data persistence
    user_interface._initialize_session_state()

    # Header Container - Contains header and search
    user_interface.display_header()
    symbol, search_clicked = user_interface.show_stock_search()

    # Handle new stock search
    if symbol and search_clicked:
        if analyzer.validate_stock_symbol(symbol):
            with user_interface.show_loading(f"📊 Analyzing {symbol}..."):
                hist_data, stock_info = analyzer.get_stock_data(
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

        with user_interface.create_stock_data_container():
            # Display all stock analysis components
            user_interface.display_real_time_indicator()
            user_interface.display_stock_overview(
                current_symbol, stock_info, hist_data)
            user_interface.display_charts(current_symbol, hist_data, "1y")
            user_interface.display_financial_metrics(stock_info, hist_data)
            user_interface.display_performance_metrics(hist_data)
            user_interface.display_company_info(stock_info)
            user_interface.display_description(stock_info)


# Run the app
if __name__ == "__main__":
    main()
