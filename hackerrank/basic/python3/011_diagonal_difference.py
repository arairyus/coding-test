#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    pri_diagonal = 0
    sec_diagonal = 0
    
    pri_index = 0
    sec_index = len(arr[0]) - 1
    for list in arr:
      pri_diagonal += list[pri_index]
      sec_diagonal += list[sec_index]
      
      pri_index += 1
      sec_index -= 1
    
    result = abs(pri_diagonal - sec_diagonal)
      
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()