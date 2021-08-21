# ========================
#       Information
# ========================

# problem link : https://www.hackerrank.com/challenges/30-operators/problem
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

#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#

def solve(meal_cost, tip_percent, tax_percent):
    # Write your code here
    meal_cost=meal_cost
    tip_percent=meal_cost*(tip_percent/100)
    tax_percent=meal_cost*(tax_percent/100)
    s=(meal_cost,tip_percent,tax_percent)
    print(int(round(sum(s),0)))

if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)
