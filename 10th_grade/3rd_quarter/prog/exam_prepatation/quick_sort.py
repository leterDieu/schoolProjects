from typing import List
import random


def choose_pivot(arr: List[float]) -> int:
    return random.randint(0, len(arr) - 1)


def quick_sort(arr: List[float]) -> List[float]:
    arr_length = len(arr)
    if arr_length <= 1:
        return arr

    pivot_index = choose_pivot(arr)
    pivot = arr[pivot_index]
    arr_left = []
    arr_right = []
    for i, el in enumerate(arr):
        if i == pivot_index:
            continue
        if el <= pivot:
            arr_left.append(el)
            continue
        arr_right.append(el)

    arr_left_sorted = quick_sort(arr_left)
    arr_right_sorted = quick_sort(arr_right)
    arr_left_sorted.append(pivot)
    arr_left_sorted.extend(arr_right_sorted)
    return arr_left_sorted
