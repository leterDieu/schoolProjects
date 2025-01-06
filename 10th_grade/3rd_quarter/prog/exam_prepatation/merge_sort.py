from typing import List


def merge(arr1: List[float], arr2: List[float]) -> List[float]:
    arr = []
    arr1_length = len(arr1)
    arr2_length = len(arr2)

    for i in range(arr2_length):
        if arr1[i] < arr2[i]:
            arr.append(arr1[i])
            arr.append(arr2[i])
            continue

        arr.append(arr2[i])
        arr.append(arr1[i])

    if arr1_length > arr2_length:
        arr.append(arr1[-1])

    return arr

def merge_sort(arr: List[float]) -> List[float]:
    arr_length = len(arr)
    if arr_length > 1:
        half = arr_length - arr_length // 2
        arr1 = merge_sort(arr[:half])
        arr2 = merge_sort(arr[half:])
        arr = merge(arr1, arr2)
    return arr
