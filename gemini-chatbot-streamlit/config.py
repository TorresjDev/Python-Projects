"""
Configuration file
Handles environment setup and API configuration
"""

import os
from dotenv import load_dotenv
import google.generativeai as genai


class Config:
    """Configuration class"""

    def __init__(self):
        """Constructor method for initializing the Config class"""
        self.api_key = None
        self.model_name = None
        self.model = None

    def load_environment(self):
        """Load environment variables from .env file"""
        load_dotenv()

        # Get API key
        self.api_key = os.getenv("GOOGLE_API_KEY")
        if not self.api_key:
            return False, "Please set your GOOGLE_API_KEY in the .env file"

        # Get model name
        self.model_name = os.getenv("GEMINI_MODEL", "gemini-2.0-flash")
        return True, "Environment loaded successfully"

    def setup_ai_model(self):
        """Setup the Gemini AI model"""
        try:
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel(self.model_name)
            return True, "AI model configured successfully"
        except Exception as e:
            return False, f"Error setting up AI: {str(e)}"
