import threading
import requests
import time

def download_file(url, index):
    response = requests.get(url)
    with open(f'file_{index}.html', 'wb') as f:
        f.write(response.content)

def sequential_download(urls):
    for i, url in enumerate(urls):
        download_file(url, i)

def threaded_download(urls):
    threads = []
    for i, url in enumerate(urls):
        t = threading.Thread(target=download_file, args=(url, i))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

if __name__ == "__main__":
    urls = [
        "https://www.example.com",
        "https://www.example.org",
        "https://www.example.net"
    ]

    start = time.time()
    sequential_download(urls)
    end = time.time()
    print(f"Sequential Download Time: {end - start:.4f} seconds")

    start = time.time()
    threaded_download(urls)
    end = time.time()
    print(f"Threaded Download Time: {end - start:.4f} seconds")

