from math import *
n = int(input())
s = 0

if __name__ == '__main__':
    for i in range(1,isqrt(n)+1):
        if n % i == 0:
            s += i
            if i != n//i:
                s += n//i
    print(s)

# 1 2 4 8 16