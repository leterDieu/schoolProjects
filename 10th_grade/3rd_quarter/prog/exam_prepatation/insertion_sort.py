from typing import List

def insertion_sort(arr: List[float]) -> List[float]:
    for i, elem in enumerate(arr[1:]):
        j = i
        while j >= 0 and elem < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = elem

    return arr
