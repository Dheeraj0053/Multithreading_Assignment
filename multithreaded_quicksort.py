import threading
import time

# Standard quicksort
def quicksort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quicksort(arr, low, p-1)
        quicksort(arr, p+1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

# Multithreaded quicksort
def threaded_quicksort(arr, low, high, max_threads=4):
    if low < high:
        p = partition(arr, low, high)

        threads = []
        if threading.active_count() < max_threads:
            t1 = threading.Thread(target=threaded_quicksort, args=(arr, low, p-1, max_threads))
            t1.start()
            threads.append(t1)
        else:
            quicksort(arr, low, p-1)

        if threading.active_count() < max_threads:
            t2 = threading.Thread(target=threaded_quicksort, args=(arr, p+1, high, max_threads))
            t2.start()
            threads.append(t2)
        else:
            quicksort(arr, p+1, high)

        for t in threads:
            t.join()

if __name__ == "__main__":
    import random
    arr = [random.randint(0, 100000) for _ in range(10000)]
    arr_copy = arr.copy()

    start = time.time()
    quicksort(arr, 0, len(arr)-1)
    end = time.time()
    print(f"Single-threaded Quicksort Time: {end - start:.4f} seconds")

    start = time.time()
    threaded_quicksort(arr_copy, 0, len(arr_copy)-1)
    end = time.time()
    print(f"Multi-threaded Quicksort Time: {end - start:.4f} seconds")
