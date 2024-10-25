import numpy as np


def vectorised_1(arr: np.ndarray[np.ndarray[float]]) -> float:
    '''
    return the sum of non-negative values on a diagonal.
    if there's none, return -1
    '''
    arr = np.diagonal(arr)
    arr = arr[arr >= 0]
    if len(arr):
        return np.sum(arr)
    return -1


def vectorised_2(arr1: np.ndarray[float], arr2: np.ndarray[float]) -> bool:
    '''
    return that two vectors are the same multi-set
    '''
    return np.array_equal(np.sort(arr1), np.sort(arr2))


def vectorised_3(arr: np.ndarray[float]) -> bool:
    '''
    return max product of any two neighbour values which's divisble by 3.
    if there's none, return -1
    '''

    temp_arr = arr * np.r_[arr[1:], arr[0]]
    return np.max(temp_arr[temp_arr % 3 == 0])


def vectorised_4(image: np.ndarray[np.ndarray[np.ndarray[float]]],
                 weights: np.ndarray[float]) -> np.ndarray[np.ndarray[float]]:
    '''
    return max product of any two neighbour values which's divisble by 3.
    if there's none, return -1
    '''

    return np.sum(image * weights, axis=2)


def vectorised_5(arr1: np.ndarray[np.ndarray[float]], arr2: np.ndarray[np.ndarray[float]]) -> float:
    '''
    return scalar product of two vectors in a RLE format.
    if vectors are different sized, return -1
    '''

    try:
        return np.dot(np.repeat(arr1[:, 0], arr1[:, 1]),
                      np.repeat(arr2[:, 0], arr2[:, 1]))
    except ValueError:
        return -1
