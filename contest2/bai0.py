
n = int(input())

for i in range (n):
    print(i+1, end=" ")
print()

for i in range(n, -1, -1):
    print(i,end=" ")
print()

for i in range(0,n + 1, 2):
    print(i, end=" ")
print()

for i in range(1,n+1,2):
    print(i, end=" ")
print()

for i in range(0,n,4 ):
    print(i, end=" ")
print()

for i in range(n):
    print(chr(97+i).lower(), end=" ")
print()

for i in range(n-1,-1,-1):
    print(chr(122-i).lower(), end= " ")
print()


