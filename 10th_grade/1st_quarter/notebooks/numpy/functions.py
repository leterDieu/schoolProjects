import numpy as np
from typing import List


def default_1(arr: List[List[float]]) -> float:
    '''
    return the sum of non-negative values on a diagonal.
    if there's none, return -1
    '''

    if not len(arr):
        return -1
    contains_non_negative = False
    summed = 0
    for i, el in enumerate(arr[:len(arr[0])]):
        if el[i] >= 0:
            summed += el[i]
            contains_non_negative = True

    return summed if contains_non_negative else -1


def default_2(arr1: List[float], arr2: List[float]) -> bool:
    '''
    return that two vectors are the same multi-set
    '''

    return sorted(arr1) == sorted(arr2)


def default_3(arr: List[float]) -> float:
    '''
    return max product of any two neighbour values 
    which's divisble by 3.
    if there's none, return -1
    '''

    max_product = -float('inf')
    for i, el in enumerate(arr[:-1]):
        temp_product = el * arr[i+1]
        if not temp_product % 3 and temp_product > max_product:
            max_product = temp_product

    return -1 if max_product == -float('inf') else max_product


def default_4(image: List[List[List[float]]],
              weights: List[float]) -> List[List[float]]:
    '''
    return corresponding sums of channels of given weight (in the image)
    (in a matrix of height x width format)
    '''

    arr = []
    for el1 in image:
        arr2 = [0] * len(weights)
        for i, el2 in enumerate(el1):
            for j, el3 in enumerate(el2):
                arr2[i] += el3 * weights[j]
        arr.append(arr2)

    return arr


def default_5(arr1: List[List[float]], arr2: List[List[float]]) -> float:
    '''
    return scalar product of two vectors in a RLE format.
    if vectors are different sized, return -1
    '''

    try:
        vec1, vec2 = [], []
        for el in arr1:
            vec1.extend([el[0]] * el[1])
        for el in arr2:
            vec2.extend([el[0]] * el[1])

        return sum([el * vec2[i] for i, el in enumerate(vec1)])
    except:
        return -1
