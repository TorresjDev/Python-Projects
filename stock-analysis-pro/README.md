# 📈 Stock Analysis Pro

**Real-Time Stock Market Analysis Dashboard**

A comprehensive, professional-grade stock analysis application that provides real-time market data, interactive charts, and detailed financial insights in a modern style User Interface.

![Status](https://img.shields.io/badge/Status-Live-green)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.48+-red)

## 🌐 Live Streamlit Application

**Click here:** [**Stock Analysis Pro - Live Demo**](https://stock-analysis-pro.streamlit.app/)

✨ _Experience a professional stock analysis directly in your browser!_

## ✨ Features

- 🔄 **Real-time updates** every 10 seconds
- 📊 **Interactive charts** with multiple timeframes
- 📈 **Technical indicators** (RSI, MACD, Moving Averages)
- 💹 **Comprehensive statistics** (P/E, Beta, Market Cap)
- 🎨 **Professional UI** inspired by modern trading platforms
- 📱 **Responsive design** for all devices
- ⚡ **Fast data retrieval** using yfinance API
- 📋 **Detailed company information** and business summaries

## 📁 Project Structure

**Simplified & Modular Architecture:**

```
stock-analysis-pro/
├── main.py              # 🚀 Application entry point
├── config.py            # ⚙️ Configuration & environment setup
├── stock_analyzer.py    # 📊 Core analysis logic & data processing
├── ui.py                # 🎨 All UI components & interface elements
├── requirements.txt     # 📦 Dependencies
└── .env                 # 🔐 Environment variables
```

**Clean Separation of Concerns:**

- **main.py** - Orchestrates the application flow
- **config.py** - Manages all configuration and environment setup
- **stock_analyzer.py** - Handles stock data analysis and processing
- **ui.py** - Contains all Streamlit interface components
-

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository:**

```bash
git clone https://github.com/TorresjDev/Python-Programs.git
cd Python-Programs/stock-analysis-pro
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Set up environment variables:**

```bash
# Copy .env.example to .env and add your API keys
cp .env.example .env
```

4. **Run the application:**

```bash
streamlit run main.py
```

5. **Open your browser:**
   Navigate to `http://localhost:8501`

**OR**

**Try the live version:** [**Stock Analysis Pro**](https://stock-analysis-pro.streamlit.app/) _(No installation required!)_

## 🛠️ Technology Stack

- **Frontend:** Streamlit
- **Data Source:** yfinance, CoinMarketCap API
- **Charts:** Plotly & Plotly Express
- **Data Processing:** Pandas, NumPy
- **Environment:** Python-dotenv

## 🙏 Acknowledgments

- **yfinance** - For providing reliable stock market data
- **Streamlit** - For the excellent web app framework
- **Plotly** - For interactive charting capabilities
- **CoinMarketCap** - For cryptocurrency data integration

---

⭐ **Star this repository if you find it helpful!**
