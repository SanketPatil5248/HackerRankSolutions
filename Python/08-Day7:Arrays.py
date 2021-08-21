# ========================
#       Information
# ========================

# problem link : https://www.hackerrank.com/challenges/30-arrays/problem
# Language: Python

# ========================
#         Solution
# ========================

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    
    # arr=sorted(arr,reverse=True)
    arr=reversed(arr)
    for i in arr:
        print(i,end = ' ')
