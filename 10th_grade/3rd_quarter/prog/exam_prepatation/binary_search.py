from typing import List


def binary_search(arr: List[float], elem: float, left: float = 0, right: float = -1) -> int:
    if right == -1:
        right = len(arr) - 1

    if right >= left:
        middle = int(left + (right - left) // 2)

        if arr[middle] == elem:
            return middle

        if arr[middle] > elem:
            return binary_search(arr, elem, left, middle - 1)

        return binary_search(arr, elem, middle + 1, right)

    return -1
