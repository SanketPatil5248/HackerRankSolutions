# ========================
#       Information
# ========================

# problem link : https://www.hackerrank.com/challenges/30-binary-numbers/problem
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
    
# Recursive fuction for convrting decimal to binary    
# def DecToBin(n):
#     if n>=1:
#         DecToBin(n//2)
#         print(n%2, end='')
# DecToBin(n)
rem=[]
while(n>0):
    rm=n%2
    n=n//2
    rem.append(rm)
    
count,result=0,0
    #printing binary values
    # for i in rem:
    #     print(i,end='')        
for i in range(0,len(rem)):
    if rem[i]==0: # if 0 then count again replaced to zero though it,s max count stored in its previous iteration in result variable.
        count=0
    else:
        count+=1
        result=max(result,count)
print(result)
            
