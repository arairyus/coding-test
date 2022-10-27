#!/bin/python3

from distutils.log import error
import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    sort_array = sorted(arr)
    min = sum(sort_array[:-1])
    max = sum(sort_array[1:])
    
    print('%d %d' %(min,max))
      

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
