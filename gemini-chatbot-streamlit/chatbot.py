"""
ChatBot class
Handles chat logic and conversation memory
"""


class ChatBot:
    """Simple chatbot for conversation logic"""

    def __init__(self, ai_model):
        """Initialize chatbot with AI model"""
        self.model = ai_model

    def build_context(self, messages):
        """Build conversation context for better memory"""

        # If no messages, return empty context
        if len(messages) == 0:
            return ""
        # If only one message, return its content
        elif len(messages) == 1:
            return messages[0]["content"]

        # Build context with coversation history
        context_parts = ["Recent conversation:"]

        # Limit to last 12 recent messages for context build
        recent_messages = messages[-12:]

        # Organize messages into User/AI format except the last message
        for msg in recent_messages[:-1]:
            role = "User" if msg["role"] == "user" else "AI"
            context_parts.append(f"{role}: {msg['content']}")

        # Add current message
        context_parts.append(f"User: {messages[-1]['content']} ")
        context_parts.append("AI:")

        # print(context_parts)
        return context_parts

    def get_ai_response(self, messages):
        """Get response from AI model"""
        try:
            # Build context for better memory
            context = self.build_context(messages)

            # Get AI response
            response = self.model.generate_content(context)

            if response and response.text:
                return True, response.text.strip()
            else:
                return False, "No response from AI. Please try again."

        except Exception as e:
            return False, f"Error: {str(e)}"
