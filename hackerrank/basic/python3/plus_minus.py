#!/bin/python3

import math
import os
import random
import re
import sys
from unittest import result

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    n = len(arr)
    positive_num = 0
    negative_num = 0
    zero_num = 0
    
    for element in arr:
      if element > 0:
        positive_num += 1
      elif 0 > element:
        negative_num += 1
      else:
        zero_num += 1

    print('{:.6f}'.format(positive_num/n))
    print('{:.6f}'.format(negative_num/n))
    print('{:.6f}'.format(zero_num/n))
      

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
