def quick_sort(arr, type='average'):
    if len(arr) <= 1:
        return arr
    if type == 'average':
        pivot = arr[0]
    elif type == 'best':
        pivot = arr[len(arr) // 2]
    elif type == 'worst':
        pivot = arr[len(arr) - 1]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left, type) + middle + quick_sort(right, type)
