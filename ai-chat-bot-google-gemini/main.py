from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
import requests

load_dotenv()
g_api_key = os.getenv("GOOGLE_API_KEY")

print("Google Gemini API - Image Text Extraction")

user_name = input("Hello, what shall I call you? ")

print(f"Welcome {user_name}, let's extract text from an image!")

image_path = input("Please enter the image URL: ")

# Fetch the image from the URL
image_response = requests.get(image_path, stream=True)

# Check if image was fetched successfully without errors
image_response.raise_for_status()

# Finds the image format from response request results
mime_type = image_response.headers.get('Content-Type')

# Create a Part object from the image bytes
image = types.Part.from_bytes(data=image_response.content, mime_type=mime_type)

client = genai.Client(api_key=g_api_key)

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=[
        # image part object for request
        f"Extract the text from the image, put my name {user_name} at the end of the text in a new line.",
        image
    ],
)

print(response.text)
