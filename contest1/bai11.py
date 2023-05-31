from math import *
a, b, c=  map(int , input().split())

if ((a + b) > c and ((b + c) > a) and ((a + c) > b)):
    if( a == b and a == c and b == c):
        print(1) # tam giac deu
    elif((a == b and a != c) or (a == c and a != b) or ( b == c and b !=a)):
        print(2) # tam giac can
    elif(sqrt((a**2 + b**2)) == sqrt(c**2) or sqrt((a**2 + c**2)) == sqrt(b**2) or sqrt((c**2 + b**2)) == sqrt(a**2)):
        print(3) # tam giac vuong
    else:
        print(4) # tam giac thuong
else: print('INVALID')