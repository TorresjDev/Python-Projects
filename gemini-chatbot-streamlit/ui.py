"""
UI Components
Handles all Streamlit interface elements
"""

import streamlit as st


def setup_page():
    """Setup Streamlit page configuration"""
    st.set_page_config(
        page_title="Google Gemini Chatbot",
        page_icon="🤖",
        layout="wide"
    )

    st.title("🤖 Google Gemini Chatbot")


def show_clear_button():
    """Show clear chat button if there are messages"""
    # Add clear button
    col1, col2, col3 = st.columns([2, 2, 1])
    with col3:
        if st.session_state.get("messages"):
            if st.button("🗑️ Clear Chat"):
                st.session_state.messages = []
                st.rerun()


def show_chat_history():
    """Show all previous messages"""

    # create session state for messages if it doesn't exist
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Show each message in the chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


def handle_user_input(chatbot):
    """Handle when user types something"""
    # prompt user for input
    if prompt := st.chat_input("💬 Ask me anything..."):

        # Add user message to session state for history
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Show user message
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate AI response
        with st.chat_message("ai"):
            success, response = chatbot.get_ai_response(
                st.session_state.messages)

            if success:
                st.markdown(response)
                # Add AI response to history
                st.session_state.messages.append({
                    "role": "ai",
                    "content": response
                })
            else:
                st.error(f"❌ {response}")


def show_error(message):
    """Show error message"""
    st.error(f" ⚠️ Error found: {message}")


def stop_app():
    """Stop the Streamlit app"""
    st.stop()
