# ========================
#       Information
# ========================

# problem link : https://www.hackerrank.com/challenges/30-conditional-statements/problem
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
    N = int(input().strip())
if N%2!=0:
    print("Weird")
else:
    if N in range(2,5):
        print("Not Weird")
    elif N in range(6,21):
        print("Weird")
    else:
        print("Not Weird")    
