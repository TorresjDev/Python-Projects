# 📱 Social Media Post Analysis Application

**A powerful Python tool for analyzing social media posting patterns with interactive visualizations and celebrity engagement analytics.**

Welcome to the **Social Media Post Analysis Application**!  
This comprehensive platform provides deep insights into social media behavior, featuring automated data processing, dual-mode visualizations, and professional-grade analytics perfect for marketers, researchers, and data enthusiasts.

---

## 🚀 Key Features

- **Interactive User Interface**: Welcomes users with clear instructions and prompts for both CSV data URL input and author selection.
- **Dynamic Author Selection**: Users can choose any author from the dataset for focused analysis, making it flexible for any celebrity or influencer.
- **Flexible Data Source**: Accepts custom CSV URLs or uses default environment configuration for seamless data loading.
- **Intelligent Data Pipeline**: Automatically downloads and processes social media datasets with built-in file existence checking.
- **Advanced Data Cleaning**: Removes unnecessary columns (country, id, language, latitude, longitude) for focused analysis.
- **Multi-Author Time Series Analysis**: Converts timestamps and tracks posting patterns across different social media accounts.
- **Dual Visualization Engine**: Creates both static matplotlib charts and interactive Plotly Express visualizations.
- **Personalized Celebrity Analysis**: Deep-dive into any selected author's posting patterns, engagement metrics, and content themes.
- **Engagement Analytics**: Analyzes likes and shares data with comparative trend visualization for the chosen author.
- **Advanced Text Processing**: Generates beautiful word clouds from post content with intelligent stop-word filtering.
- **Professional User Experience**: Includes welcome messages, progress updates, and friendly conclusion messages.

---

## 📊 What This Application Does

✅ **Interactive user onboarding** with welcome messages and clear instructions  
✅ **Flexible data input** - accepts custom URLs or uses environment defaults  
✅ **Smart data downloading** - automatically fetches CSV files when needed  
✅ **Comprehensive data cleaning** - removes geographic and metadata columns  
✅ **Advanced time series processing** - converts datetime formats for analysis  
✅ **Multi-author analytics** - tracks posting frequency across all social media accounts  
✅ **Dynamic author selection** - user chooses which celebrity/influencer to analyze in detail  
✅ **Personalized engagement metrics** - likes and shares analysis for the selected author  
✅ **Static visualizations** - professional matplotlib charts with grid styling  
✅ **Interactive charts** - Plotly Express with hover effects, zoom, and responsive design  
✅ **Custom text analytics** - word cloud generation from the chosen author's content  
✅ **User experience design** - progress updates and friendly conclusion messages

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

## 🎯 What Makes This Special

This isn't just another data analysis script - it's a user-friendly social media insights platform designed with real-world usability in mind. The application features an intuitive command-line interface that guides users through the entire process, from data input to author selection to final visualizations.

The dynamic author selection feature allows users to analyze any celebrity, influencer, or social media personality in the dataset. Whether you're interested in Jimmy Fallon's posting patterns, Taylor Swift's engagement metrics, or any other author's social media behavior, this tool adapts to your research needs - making it invaluable for social media managers, brand strategists, entertainment analysts, or academic researchers studying digital communication patterns.

**Key differentiators:**

- **Dynamic author selection** - analyze any personality in your dataset, not just pre-coded examples
- **Environment-aware configuration** for seamless deployment
- **Professional user experience** with guided prompts and status updates
- **Dual-mode visualization** combining static publication-quality charts with interactive web-ready plots
- **Flexible celebrity analytics** demonstrating real-world entertainment industry applications
- **Personalized engagement metrics** tailored to your chosen author's posting frequency and audience interaction

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
   - Choose any author from the dataset for personalized analysis (e.g., 'jimmyfallon', 'taylorswift13', etc.)
   - Enjoy the automated analysis and visualizations tailored to your selected author!

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
