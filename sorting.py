import random as rd

def distribution_counting(array):
    A = array
    n = len(A)
    l, u = min(A), max(A)
    value = u - l + 1
    d = [0] * value
    s_array = [0] * n

    for i in range(n):
        d[A[i] - l] += 1
    for j in range(1, value):
        d[j] += d[j - 1]
    for i in range(n - 1, -1, -1):
        idx = A[i] - l
        s_array[d[idx] - 1] = A[i]
        d[idx] -= 1
    return s_array


def comparison_counting(array):
    A = array
    n = len(A)
    count = [0] * n
    result = [None] * n

    for i in range(n):
        for j in range(n):
            if A[j] < A[i] or (A[j] == A[i] and j < i):
                count[i] += 1

    for i in range(n):
        result[count[i]] = A[i]

    return result


def bubble_sort(array):
    A = array.copy()
    n = len(A)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if A[j + 1] < A[j]:
                A[j], A[j + 1] = A[j + 1], A[j]
    return A


def selection_sort(array):
    A = array.copy()
    n = len(A)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if A[j] < A[min_idx]:
                min_idx = j
        A[i], A[min_idx] = A[min_idx], A[i]
    return A


def hoare_partition(A, l, r):
    p = A[l]
    i = l
    j = r + 1
    while True:
        while True:
            i += 1
            if i >= r or A[i] >= p:
                break
        while True:
            j -= 1
            if j <= l or A[j] <= p:
                break
        if i >= j:
            break
        A[i], A[j] = A[j], A[i]
    A[l], A[j] = A[j], A[l]
    return j


def quicksort(A, l, r):
    if l < r:
        s = hoare_partition(A, l, r)
        quicksort(A, l, s - 1)
        quicksort(A, s + 1, r)


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def heap_sort(arr):
    def heapify(n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and arr[l] > arr[largest]:
            largest = l
        if r < n and arr[r] > arr[largest]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(n, largest)

    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(i, 0)


if __name__ == "__main__":
    n = int(input("Enter the number of elements: "))
    lo = int(input("Enter min random value: "))
    hi = int(input("Enter max random value: "))
    arr = [rd.randint(lo, hi) for _ in range(n)]
    print(f"\nOriginal Array: {arr}\n")

    print(f"Distribution Counting Sort: {distribution_counting(arr.copy())}")
    print(f"Comparison Counting Sort: {comparison_counting(arr.copy())}")
    print(f"Bubble Sort: {bubble_sort(arr.copy())}")
    print(f"Selection Sort: {selection_sort(arr.copy())}")
    
    arr_q = arr.copy()
    quicksort(arr_q, 0, len(arr_q) - 1)
    print(f"Quick Sort: {arr_q}")
    
    arr_m = arr.copy()
    merge_sort(arr_m)
    print(f"Merge Sort: {arr_m}")
    
    arr_i = arr.copy()
    insertion_sort(arr_i)
    print(f"Insertion Sort: {arr_i}")
    
    arr_h = arr.copy()
    heap_sort(arr_h)
    print(f"Heap Sort: {arr_h}")
