# 📈 Stock Data Application

Welcome to the **Stock Data Application**!  
This project is a user-friendly web app built with [Streamlit](https://streamlit.io/) and [yfinance](https://github.com/ranaroussi/yfinance), designed to help you explore historical stock prices and company information with ease.

---

## 🌐 Live Demo

You can view the application live here:
[Stock Data Application on Streamlit Cloud](https://python-programs-v9puvb4eqw5cfalfr8qgdi.streamlit.app/)

---

## 🚀 Features

- **Interactive Web UI**: Powered by Streamlit for instant feedback and easy navigation.
- **Live Stock Data**: Fetches historical stock prices from Yahoo Finance using `yfinance`.
- **Company Insights**: Displays sector, industry, and a business summary for selected stocks.
- **Custom Date Range**: Choose your own start and end dates for data analysis.
- **Beautiful Charts**: Visualize Open, High, Low, and Close prices with interactive line charts.
- **Streaming Summaries**: Enjoy a smooth, animated display of business summaries.

---

## 🛠️ How to Run Locally

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/Python-Programs.git
   cd Python-Programs/stock-data-app
   ```

2. **Install dependencies**  
   Make sure you have Python 3.8+ installed.

   ```bash
   pip install -r requirements.txt
   ```

3. **Start the app**

   ```bash
   streamlit run main.py
   ```

4. **Open in your browser**  
   Streamlit will provide a local URL (usually [http://localhost:8501](http://localhost:8501)).

---

## 📂 Folder Structure

```
stock-data-app/
│
├── main.py             # Streamlit app source code
├── requirements.txt    # Python dependencies
└── README.md           # This documentation
```

---

## 📊 Supported Stocks

Choose from a curated list of popular stocks:

- Microsoft (MSFT)
- Apple (AAPL)
- Amazon (AMZN)
- Google (GOOGL)
- Tesla (TSLA)
- Meta (META)
- Netflix (NFLX)
- Nvidia (NVDA)
- Palantir (PLTR)

---

## 🌐 Deployment

This app can be deployed for free using [Streamlit Community Cloud](https://streamlit.io/cloud):

1. Push this folder to your GitHub repository.
2. Go to [Streamlit Cloud](https://streamlit.io/cloud) and connect your repo.
3. Set the app path to `stock-data-app/main.py`.
4. Click **Deploy**!

---

## 📚 References

- [Streamlit Documentation](https://docs.streamlit.io/library/api-reference)
- [yfinance Documentation](https://ranaroussi.github.io/yfinance/index.html)

---

## 🙏 Acknowledgements

This application was adapted and deployed by **Jesus Torres** as an assignment for the CIDM 4310/5310 Business Intelligence and Decision Support Systems course at West Texas A&M University, under the guidance of Dr. Cheng (Carl) Zhang.

- The original codebase was provided as part of the course material.

Also Special thanks to the open-source community and the creators of yfinance and Plotly!

---

## 📝 License

This project is for educational and demonstration purposes.
