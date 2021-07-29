#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#https://www.hackerrank.com/challenges/strange-advertising/problem

def viralAdvertising(n):
    
    res = 0
    views = 5
    
    for i in range(n):
        views = int(views// 2)
        res += views
        views *= 3
        
        
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
