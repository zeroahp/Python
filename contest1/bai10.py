a,b,c = map(int, input().split())

if( a > 0 and b > 0 and c >0):
    if ((a+b) > c and ((b+c) > a) and ((a+c) > b)):
        print('YES')
    else: print('NO')
else: print('NO')