import concurrent.futures
import requests
import threading
import time
import os

thread_local = threading.local()

def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()

    return thread_local.session

def download_site(url):
    session = get_session()
    with session.get(url) as response:
        indicator = "J" if "jython" in url else "R"
        print(indicator, sep='', end='', flush=True)

def download_all_sites(sites):
    recommended_workers = min(32, os.cpu_count() + 4)
    with concurrent.futures.ThreadPoolExecutor(max_workers=12) as executor:
        executor.map(download_site, sites)

if __name__ == '__main__':
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80

    print("Starting downloads")
    start = time.time()
    download_all_sites(sites)
    duration = time.time() - start
    print(f"\nDownloaded {len(sites)} sites in {duration} seconds")