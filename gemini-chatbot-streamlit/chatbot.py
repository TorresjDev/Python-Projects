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

        # If this is the first message, just return it
        if len(messages) <= 1:
            return messages[-1]["content"]

        # Build simple context with recent messages
        context_parts = ["Here's our conversation so far:"]

        # Get last 10 messages (5 exchanges)
        recent_messages = messages[-10:]

        # Add each message to context
        for msg in recent_messages[:-1]:  # Don't include current message
            role = "You" if msg["role"] == "user" else "Me"
            context_parts.append(f"{role}: {msg['content']}")

        # Add current message
        current_msg = messages[-1]["content"]
        context_parts.append(f"You: {current_msg}")
        context_parts.append("Me:")

        return "\n".join(context_parts)

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
