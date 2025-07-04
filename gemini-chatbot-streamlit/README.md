# Gemini Chatbot with Streamlit 🤖�

A **multi-turn conversational chatbot** built with **Python**, **Streamlit**, and the **Google Gemini API**. This application provides an intuitive web interface for chatting with Google's advanced Gemini AI models.

## 📌 Project Status

✅ Initial setup complete  
✅ Basic chatbot flow working  
✅ Environment configuration implemented  
✅ Multi-turn conversation support  
🛠️ Still under development – new features being added

## ✨ Features

- **Interactive Web Interface**: Clean, modern Streamlit UI for seamless conversations
- **Google Gemini Integration**: Powered by Gemini 2.0 Flash (configurable model)
- **Multi-turn Conversations**: Maintains chat history throughout the session
- **Environment Configuration**: Flexible model and API key management via `.env` file
- **Error Handling**: Graceful error handling with user-friendly messages
- **Real-time Responses**: Instant AI responses with streaming-like experience

## 🛠️ Tech Stack

- **Python 3.8+**
- **Streamlit** - Web framework for the UI
- **Google Generative AI** - Gemini API integration
- **python-dotenv** - Environment variable management

## 🚀 Quick Start

### 1. Prerequisites

- Python 3.8 or higher
- Google API key for Gemini (get one from [Google AI Studio](https://makersuite.google.com/app/apikey))

### 2. Installation

Clone the repository and install dependencies:

```bash
# Install required packages
pip install -r requirements.txt
```

### 3. Environment Setup

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_api_key_here
GEMINI_MODEL=gemini-2.0-flash
```

**Available Models:**

- `gemini-2.0-flash` (default, latest)
- `gemini-1.5-pro`
- `gemini-1.5-flash`

### 4. Run the Application

```bash
streamlit run main.py
```

The app will open in your browser at `http://localhost:8501`

## 📁 Project Structure

```
gemini-chatbot-streamlit/
├── main.py              # Main application file
├── requirements.txt     # Python dependencies
├── README.md           # Project documentation
└── .env                # Environment variables (create this)
```

## 🎯 Usage

1. **Start the application** using `streamlit run main.py`
2. **Enter your message** in the chat input at the bottom
3. **Receive AI responses** powered by Google Gemini
4. **Continue the conversation** - the app remembers your chat history
5. **Refresh to start over** - each session maintains its own conversation

## ⚙️ Configuration

### Model Selection

Change the AI model by updating your `.env` file:

```env
GEMINI_MODEL=gemini-1.5-pro  # Switch to a different model
```

### API Key Management

Ensure your Google API key has access to the Gemini API and sufficient quota.

## 🐛 Troubleshooting

**Common Issues:**

1. **"Error generating response"**

   - Check your `GOOGLE_API_KEY` in the `.env` file
   - Verify your API key has Gemini API access
   - Ensure you have sufficient API quota

2. **"Module not found"**

   - Run `pip install -r requirements.txt`
   - Ensure you're in the correct directory

3. **App won't start**
   - Check that Python 3.8+ is installed
   - Verify Streamlit installation: `streamlit --version`

## 📚 References

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Google Generative AI (Gemini) API](https://ai.google.dev/)
- [python-dotenv](https://saurabh-kumar.com/python-dotenv/)
- [Google AI Studio (API Key)](https://makersuite.google.com/app/apikey)

---

## 🙏 Acknowledgements

This application was developed by **Jesus Torres** utilizing modern data science tools and visualization libraries.

Special thanks to the open-source community and the creators of Pandas, Matplotlib, Plotly, and WordCloud!

---

## 📝 License

This project is for educational and demonstration purposes.
