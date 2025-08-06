# utils/config.py
import os

FILE_TYPES = {
    "video": [".mkv", ".mp4", ".avi", ".mov", ".wmv", ".flv"],
    "audio": [".mp3", ".wav", ".flac", ".aac", ".ogg"],
    "image": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "document": [".pdf", ".docx", ".txt", ".doc"],
    "other": []
}

# Use os.path to navigate up one directory (from utils/ to web-scraper/)
BASE_SAVE_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "downloads")

SAVE_PATHS = {
    "video": os.path.join(BASE_SAVE_PATH, "videos"),
    "audio": os.path.join(BASE_SAVE_PATH, "audio"),
    "image": os.path.join(BASE_SAVE_PATH, "images"),
    "document": os.path.join(BASE_SAVE_PATH, "documents"),
    "other": os.path.join(BASE_SAVE_PATH, "other")
}

for path in SAVE_PATHS.values():
    os.makedirs(path, exist_ok=True)