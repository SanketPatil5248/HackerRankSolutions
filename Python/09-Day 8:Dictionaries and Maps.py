# ========================
#       Information
# ========================

# problem link : https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem
# Language: Python

# ========================
#         Solution
# ========================

# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
dict={}
#reading items in dictionary
for i in range(n):
    text=input().split()
    dict[text[0]]=text[1]

while(True):
    try:
        name= input()
        if name in dict:
            print(name+"="+dict[name])
        else :
            print("Not found")
    except EOFError:
        break        

