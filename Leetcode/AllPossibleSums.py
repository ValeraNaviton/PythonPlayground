#!/bin/python3

import math
import os
import random
import re
import sys

#https://www.hackerrank.com/challenges/manasa-and-stones/problem
# Complete the 'stones' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER a
#  3. INTEGER b
#

def stones(n, a, b):
    i = 0
    summa = 0
    result = []
    lastValue = 0
    if a == b:
        result.append((n - 1) * a)
        return result

    while i < n:

        if a >= b:
            summa = (n - i - 1) * b + i * a
        else:
            summa = (n - i - 1) * a + i * b

        if i > 0 and summa == lastValue:
            lastValue = result[i]
            continue
        else:
            lastValue = summa
            result.append(summa)

        i += 1

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        a = int(input().strip())

        b = int(input().strip())

        result = stones(n, a, b)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
