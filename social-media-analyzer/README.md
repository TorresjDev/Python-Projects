# 📱 Social Media Post Analysis Application

**A powerful Python tool for analyzing social media posting patterns with interactive visualizations and celebrity engagement analytics.**

Welcome to the **Social Media Post Analysis Application**!  
This comprehensive platform provides deep insights into social media behavior, featuring automated data processing, dual-mode visualizations, and professional-grade analytics perfect for marketers, researchers, and data enthusiasts.

---

## 🚀 Key Features

- **Interactive User Interface**: Welcomes users with clear instructions and prompts for CSV data URL input with fallback to environment variables.
- **Flexible Data Source**: Accepts custom CSV URLs or uses default environment configuration for seamless data loading.
- **Intelligent Data Pipeline**: Automatically downloads and processes social media datasets with built-in file existence checking.
- **Advanced Data Cleaning**: Removes unnecessary columns (country, id, language, latitude, longitude) for focused analysis.
- **Multi-Author Time Series Analysis**: Converts timestamps and tracks posting patterns across different social media accounts.
- **Dual Visualization Engine**: Creates both static matplotlib charts and interactive Plotly Express visualizations.
- **Focused Celebrity Analysis**: Deep-dive into Jimmy Fallon's posting patterns, engagement metrics, and content themes.
- **Engagement Analytics**: Analyzes likes and shares data with comparative trend visualization.
- **Advanced Text Processing**: Generates beautiful word clouds from post content with intelligent stop-word filtering.
- **Professional User Experience**: Includes welcome messages, progress updates, and friendly conclusion messages.

---

## 🎯 What Makes This Special

This isn't just another data analysis script - it's a user-friendly social media insights platform designed with real-world usability in mind. The application features an intuitive command-line interface that guides users through the entire process, from data input to final visualizations.

The Jimmy Fallon case study showcases the application's ability to perform deep celebrity social media analysis, revealing engagement patterns, posting frequency trends, and content themes that would be invaluable for social media managers, brand strategists, entertainment analysts, or academic researchers studying digital communication patterns.

**Key differentiators:**

- **Environment-aware configuration** for seamless deployment
- **Professional user experience** with guided prompts and status updates
- **Dual-mode visualization** combining static publication-quality charts with interactive web-ready plots
- **Celebrity analytics focus** demonstrating real-world entertainment industry applications
- **Engagement metrics analysis** going beyond simple posting frequency to measure audience interaction

---

## 📂 Folder Structure

```
social-media-analyzer/
│
├── main.py             # Main analysis engine with interactive interface
├── requirements.txt    # Python dependencies
├── .env                # Environment variables (optional, user-created)
└── README.md           # This documentation
```

---

## 🛠️ How to Run

1. **Clone the repository**

   ```bash
   git clone https://github.com/TorresjDev/Python-Programs.git
   cd Python-Programs/social-media-analyzer
   ```

2. **Set up environment (Optional)**

   Create a `.env` file in the project directory:

   ```env
   CVS_URL=https://your-default-csv-url.com/data.csv
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the analysis**

   ```bash
   python main.py
   ```

5. **Follow the interactive prompts**
   - Enter a CSV URL when prompted, or press Enter to use the default from your `.env` file
   - Enjoy the automated analysis and visualizations!

---

## 📚 References

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [Plotly Express Documentation](https://plotly.com/python/plotly-express/)
- [WordCloud Documentation](https://pypi.org/project/wordcloud/)
- [python-dotenv Documentation](https://pypi.org/project/python-dotenv/)

---

## 🙏 Acknowledgements

This application was developed by **Jesus Torres** utilizing modern data science tools and visualization libraries.

Special thanks to the open-source community and the creators of Pandas, Matplotlib, Plotly, and WordCloud!

---

## 📝 License

This project is for educational and demonstration purposes.
