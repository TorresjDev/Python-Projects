"""
Stock Analysis Pro - Main Application
Entry point that orchestrates the application

"""

import config
import stock_analyzer
import ui


def main():
    """Main application function"""
    # Initialize components
    config_manager = config.Config()
    analyzer = stock_analyzer.StockAnalyzer(config_manager)
    user_interface = ui.UI(config_manager, analyzer)

    # Setup UI
    user_interface.setup_page()

    # Initialize session state for stock data persistence
    import streamlit as st
    if 'stock_data' not in st.session_state:
        st.session_state.stock_data = None
    if 'current_symbol' not in st.session_state:
        st.session_state.current_symbol = None

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
                    st.session_state.stock_data = (hist_data, stock_info)
                    st.session_state.current_symbol = symbol
                else:
                    st.error("❌ Unable to fetch stock data. Please try again.")
        else:
            user_interface.show_validation_error(symbol)

    # Stock Data Container - Contains all stock analysis components
    if st.session_state.stock_data is not None and st.session_state.current_symbol:
        hist_data, stock_info = st.session_state.stock_data
        current_symbol = st.session_state.current_symbol

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
