import asyncio
import time

async def async_upload_file(filename):
    loop = asyncio.get_event_loop()
    print(filename)
    await loop.run_in_executor(None, time.sleep, 3)
    print(f"Finished {filename}")
    return f"Uploaded {filename}"

def upload_file(filename):
    print(filename)
    time.sleep(3)
    print(f"Finished {filename}")
    return f"Uploaded {filename}"

async def upload_files(num_files):
    loop = asyncio.get_event_loop()
    tasks = []
    for num in range(num_files):
        # task = loop.run_in_executor(None, upload_file, f"File{num + 1}.txt")
        # tasks.append(task)
        tasks.append(async_upload_file(f"File{num + 1}.txt"))
    results = await asyncio.gather(*tasks, return_exceptions=True)
    print("Files uploaded:")
    print(results)


if __name__ == '__main__':

    print("Starting uploads")
    start = time.time()
    
    num_files = 40
    asyncio.run(upload_files(num_files))
    duration = time.time() - start
    print(f"\nUploaded {num_files} files in {duration} seconds")