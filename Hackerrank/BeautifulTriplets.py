#https://www.hackerrank.com/challenges/beautiful-triplets/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulTriplets' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def beautifulTriplets(d, arr):

    hashTable = {}

    n = 0
    m = 0
    output = 0

    for i in arr:
        if hashTable.get(i) is None:
            hashTable.update({i: 1})
        else:
            hashTable.update({i: hashTable.get(i) + 1})

    for k, v in hashTable.items():

        if (hashTable.get(k + d)) and (hashTable.get(k + 2 * d)):
            m = hashTable.get(k + d)
            n = hashTable.get(k + d * 2)
            output = output + m * n * v

    return output
        
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
