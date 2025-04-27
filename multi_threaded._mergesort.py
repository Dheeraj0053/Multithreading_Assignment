import threading
import time

# Standard merge sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

# Multithreaded merge sort
def threaded_merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        t1 = threading.Thread(target=threaded_merge_sort, args=(left,))
        t2 = threading.Thread(target=threaded_merge_sort, args=(right,))

        t1.start()
        t2.start()

        t1.join()
        t2.join()

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

if __name__ == "__main__":
    import random
    arr = [random.randint(0, 100000) for _ in range(10000)]
    arr_copy = arr.copy()

    start = time.time()
    merge_sort(arr)
    end = time.time()
    print(f"Single-threaded Merge Sort Time: {end - start:.4f} seconds")

    start = time.time()
    threaded_merge_sort(arr_copy)
    end = time.time()
    print(f"Multi-threaded Merge Sort Time: {end - start:.4f} seconds")
