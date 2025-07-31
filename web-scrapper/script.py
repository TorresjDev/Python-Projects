import requests
from bs4 import BeautifulSoup
import os
import re
from urllib.parse import urljoin, urlparse
from tqdm import tqdm  

def is_valid_url(url):
    """
    Checks if a URL is valid.
    """
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

def find_mkv_links(url, domain_filter=None):
    """
    Finds all potential MKV links on a page.

    Args:
        url (str): The URL of the page to scrape.
        domain_filter (str): If not none, will only include links that contain this in the url
    Returns:
        list: A list of MKV file URLs.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {url}. Error: {e}")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    mkv_links = []

    for link in soup.find_all('a', href=True):
        href = link['href']

        #make sure we are including the domain filter
        if domain_filter is not None:
            if domain_filter not in href:
                continue
            
        # Use urljoin to handle relative paths
        absolute_url = urljoin(url, href)
        
        if absolute_url.endswith('.mkv') or '.mkv?' in absolute_url: # check for things like ?dl=1
            mkv_links.append(absolute_url)

    return mkv_links


def download_file(url, save_path):
    """
    Downloads a file from a URL.

    Args:
        url (str): The URL of the file to download.
        save_path (str): The directory to save the file.
    """
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        file_name = os.path.basename(urlparse(url).path)  # Extract file name from URL

        if not file_name:
            print(f"Could not determine filename for {url}")
            return

        file_path = os.path.join(save_path, file_name)
        
        # Get total file size for the progress bar
        total_size_in_bytes = int(response.headers.get('content-length', 0))
        block_size = 8192 #8KB
        
        print(f"Starting download: {url} -> {file_path}") #start of download print

        with tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True, desc=file_name) as progress_bar:
            with open(file_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=block_size):
                    progress_bar.update(len(chunk))
                    if chunk:
                        f.write(chunk)

        print(f"Downloaded: {url} -> {file_path}")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}. Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred downloading {url}: {e}")

def main():
    """
    Main function to drive the MKV downloader.
    """
    while True:
        target_url = input("Enter the URL to scrape for MKV files: ").strip()
        if is_valid_url(target_url):
            break
        else:
            print("Invalid URL. Please enter a valid URL.")
    
    #optional domain filter
    domain_filter = input("Enter a domain filter (optional): ").strip()
    if domain_filter == "":
        domain_filter = None

    save_path = "./downloads"  # Change as needed
    os.makedirs(save_path, exist_ok=True)

    mkv_links = find_mkv_links(target_url, domain_filter)

    if not mkv_links:
        print("No MKV links found on the page.")
        return

    print(f"Found {len(mkv_links)} potential MKV links:")
    for link in mkv_links:
        print(link)

    for link in mkv_links:
        download_file(link, save_path)

    print("Finished processing links.")

if __name__ == "__main__":
    main()
