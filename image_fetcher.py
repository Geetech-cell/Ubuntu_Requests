import os
import requests
from pathlib import Path
from urllib.parse import urlparse

def get_filename(url):
    """Extract filename from URL or generate one."""
    filename = os.path.basename(urlparse(url).path)
    return filename or "image.jpg"

def download_images(urls):
    """Download images and save to Fetched_Images directory."""
    Path("Fetched_Images").mkdir(exist_ok=True)
    
    for url in urls:
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            filename = get_filename(url)
            filepath = Path("Fetched_Images") / filename
            
            with open(filepath, 'wb') as f:
                f.write(response.content)
            print(f"Saved {filename} from {url}")
            
        except requests.exceptions.RequestException as e:
            print(f"Error for {url}: {e}")

def main():
    """Prompt for URLs and download images."""
    print("Ubuntu Image Fetcher: I am because we are")
    urls = []
    while True:
        url = input("Enter URL (or press Enter to finish): ").strip()
        if not url:
            break
        urls.append(url)
    
    if urls:
        download_images(urls)
    else:
        print("No URLs provided.")

if __name__ == "__main__":
    main()