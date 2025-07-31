# utils/scraper_utils.py
from urllib.parse import urlparse, unquote  # Add unquote to the imports
import logging
import os

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("scraper.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def is_valid_url(url):
    """
    Checks if a URL is valid.
    """
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        logger.error(f"Invalid URL format: {url}")
        return False

def get_file_category(file_url, file_types):
    """
    Determines the category of a file based on its extension.
    Args:
        file_url (str): The URL of the file.
        file_types (dict): Dictionary of file types and their extensions.
    Returns:
        str: The category of the file (e.g., 'video', 'audio').
    """
    extension = os.path.splitext(urlparse(file_url).path)[1].lower()
    for category, extensions in file_types.items():
        if extension in extensions:
            return category
    return "other"

def get_user_confirmation(prompt):
    """
    Asks the user for a yes/no confirmation.
    Args:
        prompt (str): The prompt to display to the user.
    Returns:
        bool: True if the user confirms (y/yes), False otherwise.
    """
    while True:
        response = input(f"{prompt} (y/n): ").strip().lower()
        if response in ['y', 'yes']:
            return True
        elif response in ['n', 'no']:
            return False
        print("Please enter 'y' or 'n'.")

def select_files_to_download(file_links):
    """
    Allows the user to select which files to download from the list.
    Args:
        file_links (list): List of tuples (file_url, category).
    Returns:
        list: Filtered list of tuples (file_url, category) that the user wants to download.
    """
    if not file_links:
        return []

    print("\nFound the following files:")
    for idx, (file_url, category) in enumerate(file_links, 1):
        # Decode the URL for display purposes
        decoded_url = unquote(file_url)
        print(f"{idx}. {decoded_url} (Category: {category})")

    print("\nOptions:")
    print("  - Enter 'all' to download all files.")
    print("  - Enter 'none' to skip all files.")
    print("  - Enter specific numbers (e.g., '1 3 5') to select files.")
    print("  - Enter a range (e.g., '1-3') to select a range of files.")

    while True:
        choice = input("\nWhich files would you like to download? ").strip().lower()
        
        if choice == 'all':
            return file_links
        elif choice == 'none':
            return []
        else:
            selected_indices = set()
            try:
                parts = choice.split()
                for part in parts:
                    if '-' in part:
                        start, end = map(int, part.split('-'))
                        if start < 1 or end > len(file_links) or start > end:
                            raise ValueError("Invalid range.")
                        selected_indices.update(range(start - 1, end))
                    else:
                        idx = int(part) - 1
                        if idx < 0 or idx >= len(file_links):
                            raise ValueError("Invalid number.")
                        selected_indices.add(idx)
                break
            except ValueError as e:
                print(f"Error: {e}. Please try again (e.g., 'all', 'none', '1 3 5', '1-3').")

    selected_files = [file_links[idx] for idx in sorted(selected_indices)]
    return selected_files