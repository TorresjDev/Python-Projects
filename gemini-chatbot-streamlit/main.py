import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os


load_dotenv()
g_api_key = os.getenv("GOOGLE_API_KEY")
# Default fallback if not set
gemini_model = os.getenv("GEMINI_MODEL")

st.set_page_config(page_title="Google Gemini Chatbot", page_icon="🤖")

# Configure the Google Gemini API
if not g_api_key:
    st.error("Please set the GOOGLE_API_KEY environment variable.")
    st.stop()
# Configure the Google Gemini API
try:
    genai.configure(api_key=g_api_key)
except Exception as e:
    st.error(f"Error configuring Google Gemini API: {str(e)}")
    st.stop()

# Chatbot Development with Google Gemini API: build a multi-turn chatbot using the Streamlit framework

st.title("Google Gemini Chatbot")

# Set up the Google Gemini model
model = genai.GenerativeModel(gemini_model)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Hello! 👋 How can I help you?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # Generate response using Google Gemini
            response = model.generate_content(prompt)
            full_response = response.text

            # Display the response
            st.markdown(full_response)

            # Add assistant response to chat history
            st.session_state.messages.append(
                {"role": "assistant", "content": full_response})

        except Exception as e:
            st.error(f"Error generating response: {str(e)}")
            st.error("Please check your Google API key and try again.")
