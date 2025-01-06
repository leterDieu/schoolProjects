from typing import List


def bubble_sort(arr: List[float]) -> List[float]:
    arr_length = len(arr)

    for i in range(arr_length):
        swapped = False

        for j in range(arr_length - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr
