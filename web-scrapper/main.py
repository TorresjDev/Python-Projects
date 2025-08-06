# main.py
from utils.scraper_utils import is_valid_url, logger, select_files_to_download, get_user_confirmation
from utils.scraper import find_digital_files
from utils.downloader import download_file
from urllib.parse import unquote  # Add unquote to the imports

def main():
    """
    Main function to drive the web scraper and downloader.
    """
    logger.info("Starting the web scraper...")

    while True:
        target_url = input("Enter the URL to scrape for digital files: ").strip()
        if is_valid_url(target_url):
            break
        logger.warning("Invalid URL. Please enter a valid URL.")

    domain_filter = input("Enter a domain filter (optional, press Enter to skip): ").strip()
    if not domain_filter:
        domain_filter = None

    file_links = find_digital_files(target_url, domain_filter)

    if not file_links:
        logger.info("No digital files found on the page.")
        return

    selected_files = select_files_to_download(file_links)

    if not selected_files:
        logger.info("No files selected for download. Exiting.")
        return

    logger.info(f"\nYou have selected {len(selected_files)} file(s) for download:")
    for file_url, category in selected_files:
        decoded_url = unquote(file_url)
        logger.info(f"{decoded_url} (Category: {category})")

    if not get_user_confirmation("\nAre you ready to start the download process?"):
        logger.info("Download process aborted by user.")
        return

    for file_url, category in selected_files:
        download_file(file_url, category)

    logger.info("Finished processing links.")

if __name__ == "__main__":
    main()