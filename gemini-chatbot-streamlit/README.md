# Gemini Chatbot with Streamlit 🤖

Hey👋 welcome to my conversational AI chatbot using Python, Streamlit, and Google's Gemini API. What started as a simple chat interface evolved into something I'm pretty proud of - a clean, modular application that actually remembers what you talked about earlier in the conversation.

I spent a lot of time thinking about code organization here. Instead of cramming everything into one massive file, I broke it down into focused modules that each handle their own thing. It makes the code so much easier to understand and work with.

## 🚀 **Try It Live!**

**[🌐 Live Demo - Try the Chatbot Now!](https://gemini-chatbot-app-btde8kwdrhhftiappiw9nky.streamlit.app/)**

_Click the link above to interact with the chatbot directly in your browser - no setup required!_

## What This Thing Does

- **Clean Chat Interface**: Built with Streamlit, so it looks modern and works great
- **Smart Conversations**: The bot actually remembers what you said 10 messages ago
- **Easy Setup**: Just drop your API key in a `.env` file and you're good to go
- **Flexible Models**: Want to try different Gemini models? Just change one line
- **Error Handling**: When things go wrong, you get helpful messages instead of crashes
- **Session Management**: Your chat history sticks around until you decide to clear it

## 🏗️ How I Organized Everything

### **The File Structure**

I wanted each file to have one job and do it well:

- **`main.py`** - The conductor. It orchestrates everything but doesn't do the heavy lifting
- **`config.py`** - Handles all the environment setup and API configuration
- **`chatbot.py`** - The brain. Pure conversation logic with no UI clutter
- **`ui.py`** - Everything visual. All the Streamlit magic happens here

### **Why I Built It This Way**

- **Single Responsibility** - Each module has one clear job
- **Clean Dependencies** - No unnecessary imports cluttering things up
- **Easy Testing** - I can test each piece independently
- **Room to Grow** - Adding new features won't break existing code

## 🛠️ What You'll Need

- **Python 3.8+** - The foundation
- **Streamlit** - For the web interface
- **Google Generative AI** - Powers the chatbot
- **python-dotenv** - Manages environment variables

## 🚀 Getting Started

### **Option 1: Try the Live Demo (Easiest)**

Just click the [**Live Demo Link**](https://gemini-chatbot-app-btde8kwdrhhftiappiw9nky.streamlit.app/) above - no installation needed!

### **Option 2: Run Locally**

### 1. Prerequisites

You'll need Python 3.8 or higher and a Google API key for Gemini. You can get one from [Google AI Studio](https://makersuite.google.com/app/apikey) - it's free to start with.

### 2. Installation

```bash
# Install the required packages
pip install -r requirements.txt
```

### 3. Environment Setup

Create a `.env` file in the project folder:

```env
GOOGLE_API_KEY=your_google_api_key_here
GEMINI_MODEL=gemini-2.0-flash
```

**Model Options:**

- `gemini-2.0-flash` (newest, what I recommend)
- `gemini-1.5-pro` (more capable, bit slower)
- `gemini-1.5-flash` (fast and efficient)

### 4. Fire It Up

```bash
streamlit run main.py
```

Your browser should open to `http://localhost:8501` and you're ready to chat!

## 📁 Project Structure

```
gemini-chatbot-streamlit/
├── main.py              # 🎯 Application entry point
├── config.py            # ⚙️ Environment & API configuration
├── chatbot.py           # 🤖 Chat logic & conversation memory
├── ui.py                # 🎨 User interface components
├── requirements.txt     # 📦 Python dependencies
├── README.md            # 📖 Project documentation
└── .env                 # 🔐 Environment variables (create this)
```

### **Module Responsibilities**

| Module           | Purpose                              | Dependencies                          |
| ---------------- | ------------------------------------ | ------------------------------------- |
| **`main.py`**    | Entry point, orchestrates app flow   | `config`, `chatbot`, `ui`             |
| **`config.py`**  | Environment setup, API configuration | `os`, `dotenv`, `google.generativeai` |
| **`chatbot.py`** | Chat logic, conversation memory      | _None_ (pure Python logic)            |
| **`ui.py`**      | Streamlit interface components       | `streamlit`                           |

## 🎯 Usage Guide

### **Starting the Application**

1. Run `streamlit run main.py` (or try the [live demo](https://gemini-chatbot-app-btde8kwdrhhftiappiw9nky.streamlit.app/))
2. The app automatically:
   - Loads your `.env` configuration
   - Initializes the Gemini AI model
   - Sets up the chat interface

### **Chatting with the Bot**

1. **Type your message** in the input field at the bottom
2. **Press Enter** to send your message
3. **AI responds** with context from your conversation history
4. **Continue chatting** - the bot remembers your entire conversation

### **Managing Conversations**

- **Clear Chat**: Click the 🗑️ button to start a new conversation
- **Session Persistence**: Your chat history persists until you refresh or clear
- **Error Recovery**: Any errors are displayed with helpful messages

## 📦 Dependencies

Here's what gets installed when you run `pip install -r requirements.txt`:

- **`python-dotenv`** - Loads environment variables from `.env` files
- **`google-generativeai`** - Google's official Gemini API client
- **`streamlit`** - Web framework for building the chat interface
- **`requests`** - HTTP library for API calls (dependency of google-generativeai)

## ⚙️ Configuration Options

### **Switching Models**

Want to try a different Gemini model? Just update your `.env` file:

```env
GEMINI_MODEL=gemini-1.5-pro  # Switch to the Pro model
```

### **API Key Management**

- Keep your API key in the `.env` file (never commit this to git!)
- Make sure your key has Gemini API access enabled
- Check your quota if you're hitting rate limits

### **Memory Management**

The chatbot keeps track of your conversation by:

- Remembering the last 10 messages (5 back-and-forth exchanges)
- Building context for each response to maintain conversation flow
- Automatically handling long conversations by keeping the most recent stuff

## 🐛 When Things Go Wrong

**"Error loading environment"**

```bash
# Double-check your .env file has:
GOOGLE_API_KEY=your_actual_key_here
GEMINI_MODEL=gemini-2.0-flash
```

**"Error setting up AI model"**

- Make sure your Google API key is valid
- Check that Gemini API is enabled in your Google Cloud project
- Verify you haven't hit your API quota

**"Module not found errors"**

```bash
# Install everything fresh
pip install -r requirements.txt
```

**"Streamlit won't start"**

```bash
# Check if Streamlit is installed properly
streamlit --version
# Reinstall if needed
pip install streamlit --upgrade
```

**"No response from AI"**

- Check your internet connection
- Verify API key permissions
- Try switching to a different model in your `.env` file

## 🧪 Development Notes

### **Why This Structure Works**

- **Easy Testing**: Each module can be tested independently
- **Clean Development**: Work on UI, logic, or config separately
- **Team Collaboration**: Multiple people can work on different modules
- **Future Extensions**: Easy to add new features without breaking existing code

### **Extending the Application**

- **Add new UI components**: Modify `ui.py`
- **Enhance chat logic**: Update `chatbot.py`
- **Add new configuration options**: Extend `config.py`
- **Change application flow**: Modify `main.py`

## 📚 References & Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Google Generative AI (Gemini) API](https://ai.google.dev/)
- [python-dotenv Documentation](https://saurabh-kumar.com/python-dotenv/)
- [Google AI Studio (API Key)](https://makersuite.google.com/app/apikey)

## 🙏 Acknowledgements

This program was created for educational purposes as part of the Computer Information and Decision Management Business Intelligence and Decision Support Systems course at West Texas A&M University, under the guidance of Dr. Cheng (Carl) Zhang.

Also special thanks to the open-source community and the creators of Streamlit, Google Generative AI, and the Python ecosystem!

---

## 📝 License

This project is for educational and demonstration purposes, showcasing best practices in Python application development and AI integration.
