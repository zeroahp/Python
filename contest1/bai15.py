n,a,b = map(int, input().split())

r1 = (n // 1) * a
r2 = ((n // 2) * b) + + (n - ((n//2)*2))*a

if r1 < r2 :
    print(r1)
else: print(r2)
