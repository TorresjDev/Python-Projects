"""
Quick test for the crypto analyzer
"""

import config
import crypto_analyzer


def test_crypto_analyzer():
    """Test crypto analyzer functionality"""
    # Initialize config and analyzer
    config_manager = config.Config()
    analyzer = crypto_analyzer.CryptoAnalyzer(config_manager)

    print("Testing Crypto Analyzer...")
    print(
        f"API Key loaded: {'✓' if config_manager.api_keys.get('coinmarketcap') else '✗'}")

    # Test symbol validation
    print("\n=== Testing Symbol Validation ===")
    test_symbols = ["BTC", "ETH", "INVALID123"]
    for symbol in test_symbols:
        is_valid = analyzer.validate_crypto_symbol(symbol)
        print(f"{symbol}: {'✓ Valid' if is_valid else '✗ Invalid'}")

    # Test data fetching
    print("\n=== Testing Data Fetching ===")
    btc_data = analyzer.get_crypto_data("BTC")
    if btc_data:
        quote = btc_data["quote"]["USD"]
        print(f"BTC Price: ${quote['price']:.2f}")
        print(f"Market Cap: ${quote['market_cap']:,.2f}")
        print(f"24h Change: {quote['percent_change_24h']:.2f}%")
        print("✓ Data fetch successful")
    else:
        print("✗ Failed to fetch BTC data")

    print("\nTest completed!")


if __name__ == "__main__":
    test_crypto_analyzer()
