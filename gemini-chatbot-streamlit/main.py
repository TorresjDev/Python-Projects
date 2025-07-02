from pydoc import cli
import re
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
import requests
import streamlit as st


load_dotenv()
g_api_key = os.getenv("GOOGLE_API_KEY")

# Chatbot Development with Google Gemini API:  build a multi-turn chatbot using the Streamlit framework

st.title("Google Gemini Chatbot")

st.write("This is a simple chatbot built with Streamlit and Google Gemini API.")

user_input = st.text_input("You: ", "")

client = genai.Client(api_key=g_api_key)

response = None

if st.button("Send"):
    response = client.models.generate_content(
        model="gemini-2.o-flash",
        contents=[
            f"User: {user_input}",
            "Assistant: Hello! How can I assist you today?"
        ],
    )

if response:
    st.write(response.text)
else:
    st.write("No response from the chatbot.")
