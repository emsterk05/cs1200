from asyncio import base_tasks
import math
import time
import random

"""
See below for mergeSort and singletonBucketSort functions, and for the BC helper function.
"""


def merge(arr1, arr2):
    sortedArr = []

    i = 0
    j = 0
    while i < len(arr1) or j < len(arr2):
        if i >= len(arr1):
            sortedArr.append(arr2[j])
            j += 1
        elif j >= len(arr2):
            sortedArr.append(arr1[i])
            i += 1
        elif arr1[i][0] <= arr2[j][0]:
            sortedArr.append(arr1[i])
            i += 1
        else:
            sortedArr.append(arr2[j])
            j += 1

    return sortedArr

def mergeSort(arr):
    if len(arr) < 2:
        return arr

    midpt = int(math.ceil(len(arr)/2))

    half1 = mergeSort(arr[0:midpt])
    half2 = mergeSort(arr[midpt:])

    return merge(half1, half2)

def singletonBucketSort(univsize, arr):
    universe = []
    for i in range(univsize):
        universe.append([])

    for elt in arr:
        universe[elt[0]].append(elt)

    sortedArr = []
    for lst in universe:
        for elt in lst:
            sortedArr.append(elt)

    return sortedArr

def BC(n, b, k):
    if b < 2:
        raise ValueError()
    digits = []
    for i in range(k):
        digits.append(n % b)
        n = n // b
    if n > 0:
        raise ValueError()
    return digits

def radixSort(univsize, base, arr):
    """ arr[i][0] is the key K_i, arr[i][1][0] is the value V_i, arr[i][1][1] is the list of coefficients V_i' """
    n = len(arr)
    k = math.ceil(math.log(univsize) / math.log(base))

    """for each element in the array, get the coefficient list"""
    for i in range(n):
        arr[i] = [arr[i][0], (arr[i][1], BC(arr[i][0], base, k))]

    """for each digit"""
    for i in range(k):
        """go through the whole array arr and SBS the keys"""
        for j in range(n):
            """set new keys based off current digit place"""
            arr[j][0] = arr[j][1][1][i]
        arr = singletonBucketSort(base, arr)

    for i in range(n):
        arr[i][0] = 0
        for j in range(k):
            arr[i][0] += arr[i][1][1][j] * (base ** j)
        arr[i] = (arr[i][0],arr[i][1])  
    return arr
