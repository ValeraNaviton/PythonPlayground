#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#https://www.hackerrank.com/challenges/bon-appetit/problem?h_r=profile

def bonAppetit(bill, k, b):
    
    summa = 0
    
    for i in range(len(bill)):
        if i != k:
            summa = summa + bill[i]
            
    if summa/2 - b == 0:
        print("Bon Appetit")
    else:
        print(int(abs(summa/2 - b)))
        
        

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
