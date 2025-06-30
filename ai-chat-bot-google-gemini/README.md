# 🤖 AI Chat Bot with Google Gemini API

Welcome to the **AI Chat Bot - Google Gemini** project!  
This Python program uses the Google Gemini API to extract text from images, its a terminal-based application with a short conversational user interface.

---

## 🚀 Key Features

- **Conversational User Interface:** Engages the user with prompts for their name and an image URL.
- **Dynamic Image Handling:** Automatically detects the image type (e.g., PNG, JPEG) from the URL, making it flexible for different image formats.
- **Robust URL Fetching:** Includes error checking to ensure the provided URL is valid and the image can be downloaded successfully.
- **AI-Powered Text Extraction:** Leverages the Google Gemini API to accurately perform Optical Character Recognition (OCR) on the image.
- **Personalized Output:** Appends the user's name to the extracted text for a custom touch.

---

## 🗝️ Requires a Google AI Studio API Key

To use this project, you must have a valid [Google AI Studio API Key](https://aistudio.google.com/apikey).  
This key is required to authenticate requests to the Gemini API.  
Store your API key securely in a `.env` file as described below.

### 🔑 How to Create a Google AI Studio API Key

1. Go to [Google AI Studio API Keys](https://aistudio.google.com/apikey).
2. Sign in with your Google account if prompted.
3. Click the **"Create API Key"** button.
4. Copy the generated API key.
5. In your project folder, create a file named `.env` (if it doesn't exist).
6. Add the following line to your `.env` file (replace with your actual key):
   ```
   GOOGLE_API_KEY=your-google-api-key-here
   ```
   **🙏IMPORTANT: Never share your API key publicly or commit it to version control.**

---

## 🛠️ How to Run

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/Python-Programs.git
   cd Python-Programs/ai-chat-bot-google-gemini
   ```

2. **Set up your environment variables**

   - Create a `.env` file in this folder with:
     ```
      GOOGLE_API_KEY=your-google-api-key-here  # Replace with your actual API key
     ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the program in your terminal**
   ```bash
   python main.py
   ```

---

## 📂 Folder Structure

```
ai-chat-bot-google-gemini/
│
├── main.py           # Main Python script
├── requirements.txt  # Python dependencies
├── .env              # Environment variables (not tracked by git)
└── README.md         # This documentation
```

---

## 📚 References

- [Google Gemini API Documentation](https://ai.google.dev/)
- [Google Generative AI Python SDK](https://github.com/google-gemini/generative-ai-python)
- [Google AI Studio API Key](https://aistudio.google.com/apikey)
- [Google AI Image Understanding](https://ai.google.dev/gemini-api/docs/image-understanding)
- [python-dotenv Documentation](https://pypi.org/project/python-dotenv/)
- [requests Documentation](https://docs.python-requests.org/)

---

## 🙏 Acknowledgements

This project was created for educational purposes as a part of integrating Google Gemini's API with Python for the Computer Information and Decision Management Business Intelligence and Decision Support Systems course at West Texas A&M University, under the guidance of Dr. Cheng (Carl) Zhang.

Special thanks to the open-source community and the authors of the libraries used!

---

## 📝 License

This project is for educational and demonstration purposes only.
