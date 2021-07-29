#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#https://www.hackerrank.com/challenges/mini-max-sum/submissions/code/223296979



def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1
        while low <= high and array[low] <= pivot:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break

    array[start], array[high] = array[high], array[start]

    return high

def quick_sort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)

def miniMaxSum(arr):

    minimum = 0
    maximum = 0


    quick_sort(arr, 0, len(arr)-1)

    i = 0
    j = 0

    while i < len(arr)-1:
            minimum = minimum + arr[i]
            i += 1

    while j < len(arr)-1:
        j+=1
        maximum = maximum + arr[j]

    result = [minimum, maximum]

    print("%d %d" %(minimum, maximum))




if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
