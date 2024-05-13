import asyncio
import time
import aiohttp

async def download_site(session, url):
    async with session.get(url) as response:
        indicator = "J" if "jython" in url else "R"
        print(indicator, sep='', end='', flush=True)

async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.ensure_future(download_site(session, url))
            tasks.append(task)

        await asyncio.gather(*tasks, return_exceptions=True)

# Example to batch upload tasks 10 at a time
async def upload_files(tasks):
    batch_size = 10
    for i in range(0, len(tasks), batch_size):
        batch_tasks = tasks[i:i+batch_size]
        await asyncio.gather(*batch_tasks)
    

if __name__ == '__main__':
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 1000

    print("Starting downloads")
    start = time.time()
    
    asyncio.run(download_all_sites(sites))
    duration = time.time() - start
    print(f"\nDownloaded {len(sites)} sites in {duration} seconds")