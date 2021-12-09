def QuickSort(arr, low, high):
    if(low < high):
        q = Partition(arr, low, high)
        QuickSort(arr, low, q-1)
        QuickSort(arr, q+1, high)


def Partition(arr, low, high):
    pivot = arr[high]
    i = low-1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1


arr = [1, 3, 1, 3, 5, 3, 2, 1]
QuickSort(arr, 0, len(arr)-1)
print(arr)
