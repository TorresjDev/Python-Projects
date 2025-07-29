# Stock & Crypto Monitor

A simple and interactive web application to monitor stock and cryptocurrency data. Built with Python 🐍 and Streamlit 🎈, it fetches real-time data from Yahoo Finance and CoinMarketCap APIs and provides graphical insights for informed decision-making.

---

## 📂 Project Structure

```plaintext
stock_crypto_app/
│
├── data/
│   ├── raw/                     # Raw data from APIs (optional)
│   ├── processed/               # Processed data (optional)
│   └── example_data.csv         # Example datasets for initial development/testing
│
├── src/
│   ├── components/              # Reusable UI components for Streamlit
│   ├── logic/                   # Business logic and data processing
│   └── app.py                   # Main Streamlit app entry point
│
├── tests/                         # Unit tests for APIs and logic
├── config.py                      # Configuration file for API keys, etc.
├── requirements.txt               # Python dependencies
├── README.md                      # Project overview and setup instructions
└── .gitignore                     # Git ignored files and directories
```

---

## 🛠️ Setup Instructions

### **1. Clone the Repository**

```bash
git clone https://github.com/your-username/stock_crypto_app.git
cd stock_crypto_app
```

### **2. Set Up the Virtual Environment**

Create and activate a Python virtual environment to isolate dependencies.

#### Create a Virtual Environment

```bash
python -m venv venv
```

#### Activate the Virtual Environment

- **On Windows (Git Bash or PowerShell)**:
  ```bash
  source venv/Scripts/activate
  ```
- **On macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

You should see `(venv)` in your terminal prompt, indicating the environment is active.

---

### **3. Install Dependencies**

Install all required libraries listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

### **4. Run the Streamlit App**

Start the app locally using Streamlit:

```bash
streamlit run app.py
```

- After running this command, the app will open in your default browser at `http://localhost:8501`.

---

## 🧩 Features

- Fetch stock data (e.g., AAPL, TSLA) using Yahoo Finance.
- Fetch cryptocurrency prices (e.g., BTC, ETH) using CoinMarketCap.
- Visualize trends with interactive charts.

---

## 🚀 Future Enhancements

- Add buy/sell signal recommendations.
- Include more advanced charts (e.g., moving averages, RSI).
- Build a portfolio tracker.

---

## 🔑 API Key Configuration

1. Sign up for a free [CoinMarketCap API Key](https://coinmarketcap.com/api/).
2. Save the API key in `config.py`:

```python
# config.py
COINMARKETCAP_API_KEY = "your_api_key_here"
```

---

## 📝 Notes

- Ensure the virtual environment is activated before running or installing any Python packages.
- Always keep your `requirements.txt` file updated by running:
  ```bash
  pip freeze > requirements.txt

  ```
