# ========================
#       Information
# ========================

# problem link : https://www.hackerrank.com/challenges/30-hello-world/problem
# Language: Python

# ========================
#         Solution
# ========================

# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
#li=[]

for i in range(0,n):
    s=input()
#    li.append(s)
    
    
#for i in range(0,n):
#    for j in range(0,len(li[i]),2):
#        print(li[i][j],end='') 
#    print(end=' ')
    
#for i in range(0,n):
#    for j in range(1,len(li[i]),2):
#        print(li[i][j],end='') 
#    print(end=' ')
    
    for j in range(0,len(s),2):
        print(s[j],end='')
    print(" ",end='')
    
    for j in range(1,len(s),2):
        print(s[j],end='')
    print("")
