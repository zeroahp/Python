n = int(input())

s = 0
for i in range (1,n+1):
    s += float(1/i)
print('%.3f' % s)