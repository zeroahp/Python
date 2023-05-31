from math import *
n =  int(input())
s = 0

for i in range (1,n+1):
    s += float(1/(i*2))

print('%.5f' % s)