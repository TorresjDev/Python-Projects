"""
Google Gemini Chatbot with Streamlit
Main application entry point
"""

from config import Config
from chatbot import ChatBot
import ui


def main():
    """Main application"""
    # Setup page
    ui.setup_page()

    # Setup configuration
    config = Config()

    # Load environment
    success, message = config.load_environment()
    if not success:
        ui.show_error(message)
        ui.stop_app()

    # Setup AI model
    success, message = config.setup_ai_model()
    if not success:
        ui.show_error(message)
        ui.stop_app()

    # Create chatbot
    chatbot = ChatBot(config.model)

    # Show interface

    ui.show_chat_history()
    ui.handle_user_input(chatbot)


# Run the app
if __name__ == "__main__":
    main()
