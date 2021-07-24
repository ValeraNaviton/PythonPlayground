#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'equalizeArray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
# usage: python3  EqualizeArray.py 4 5 4 7 8
#

def equalizeArray(arr):

    hashTable = {}
    for i in arr:
        if hashTable.get(i) is None:
            hashTable.update({i: 1})
        else:
            hashTable.update({i: hashTable.get(i) + 1})

    maxVal = 0

    for k, v in hashTable.items():
        if v > maxVal:
            maxVal = v

    return len(arr) - maxVal


def main(argv):

    intArgv = []

    i = 0

    while i < len(argv) - 1:
        i += 1
        element = int(argv[i])
        intArgv.append(element)

    equalizeArray(intArgv)

    print(equalizeArray(intArgv))


if __name__ == "__main__":
    main(sys.argv)