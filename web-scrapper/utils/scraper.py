# utils/scraper.py
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, unquote, urlparse  # Add unquote to the imports
from .config import FILE_TYPES
from .scraper_utils import logger, get_file_category

def find_digital_files(url, domain_filter=None):
    """
    Finds all potential digital files on a page.
    Args:
        url (str): The URL of the page to scrape.
        domain_filter (str): If not None, only include links containing this string.
    Returns:
        list: A list of tuples (file_url, category).
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching URL {url}: {e}")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    file_links = []

    supported_extensions = set(ext for exts in FILE_TYPES.values() for ext in exts)

    for link in soup.find_all('a', href=True):
        href = link['href']
        
        if domain_filter and domain_filter not in href:
            continue

        absolute_url = urljoin(url, href)

        extension = os.path.splitext(urlparse(absolute_url).path)[1].lower()
        if extension in supported_extensions:
            category = get_file_category(absolute_url, FILE_TYPES)
            file_links.append((absolute_url, category))
            # Decode the URL for logging purposes
            decoded_url = unquote(absolute_url)
            logger.info(f"Found file: {decoded_url} (Category: {category})")

    return file_links