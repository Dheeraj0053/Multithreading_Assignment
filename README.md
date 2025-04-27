# Advanced Programming Assignment: Multithreading in Python

## Files
- `multithreaded_mergesort.py`: Multi-threaded Merge Sort implementation.
- `multithreaded_quicksort.py`: Multi-threaded Quicksort implementation.
- `concurrent_downloader.py`: Concurrent file downloader using threads.

## How to Run

### 1. Multi-threaded Merge Sort
```bash
python multithreaded_mergesort.py
```

### 2. Multi-threaded Quicksort
```bash
python multithreaded_quicksort.py
```

### 3. Concurrent File Downloader
```bash
python concurrent_downloader.py
```

## Sample Inputs and Outputs
- **Sorting Scripts:** Automatically generate random arrays of 10,000 integers.
- **Downloader:** Downloads example pages (`example.com`, `example.org`, `example.net`) and saves them as files locally.

Execution times (Single-threaded vs Multi-threaded) are displayed after running each script.

## Notes
- You can modify the size of the array or the list of URLs to test performance with larger datasets.
- `requests` library is required for the downloader script. Install it using:
```bash
pip install requests
