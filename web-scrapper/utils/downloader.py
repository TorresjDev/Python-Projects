# utils/downloader.py
import requests
import os
from urllib.parse import urlparse, unquote  # Add unquote to the imports
from tqdm import tqdm
from .config import SAVE_PATHS
from .scraper_utils import logger
import re

def sanitize_filename(filename):
    """
    Sanitizes a filename by replacing invalid characters with underscores.
    """
    # Replace invalid characters with underscores
    return re.sub(r'[<>:"/\\|?*]', '_', filename)

def download_file(file_url, category):
    """
    Downloads a file from a URL and saves it to the appropriate category folder.
    Args:
        file_url (str): The URL of the file to download.
        category (str): The category of the file (e.g., 'video', 'audio').
    """
    try:
        response = requests.get(file_url, stream=True, timeout=10)
        response.raise_for_status()

        # Extract the file name from the URL and decode it
        file_name = os.path.basename(urlparse(file_url).path)
        if not file_name:
            logger.warning(f"Could not determine filename for {unquote(file_url)}")
            return

        # Decode the file name to replace %20 with spaces, etc.
        decoded_file_name = unquote(file_name)
        # Sanitize the file name to remove invalid characters
        sanitized_file_name = sanitize_filename(decoded_file_name)
        save_path = SAVE_PATHS.get(category, SAVE_PATHS["other"])
        file_path = os.path.join(save_path, sanitized_file_name)

        total_size = int(response.headers.get('content-length', 0))
        block_size = 8192

        # Decode the URL for logging purposes
        decoded_url = unquote(file_url)
        logger.info(f"Starting download: {decoded_url} -> {file_path}")

        with tqdm(total=total_size, unit='iB', unit_scale=True, desc=decoded_file_name) as progress_bar:
            with open(file_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=block_size):
                    progress_bar.update(len(chunk))
                    if chunk:
                        f.write(chunk)

        logger.info(f"Downloaded: {decoded_url} -> {file_path}")

    except requests.exceptions.RequestException as e:
        logger.error(f"Error downloading {unquote(file_url)}: {e}")
    except Exception as e:
        logger.error(f"Unexpected error downloading {unquote(file_url)}: {e}")