def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        key = i
        for j in range(i + 1, n):
            if arr[j] < arr[key]:
                key = j
        arr[i], arr[key] = arr[key], arr[i]
    return arr
