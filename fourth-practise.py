""" Min-MAx Problem"""

import math
import os
import random
import re
import sys

# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.

def miniMaxSum(arr):
    arr.sort()
    s = sum(arr)
    maxi = s - arr[0]
    mini = s - arr[len(arr) - 1]
    print(mini,maxi)
    
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
