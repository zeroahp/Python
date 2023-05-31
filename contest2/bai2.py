from math import *
n = int(input())
s = 0
for i in range(1,n+1):
    s += pow(i,2)

print(int(s))