a, b= map(int, input().split())
print(a+b, a-b, a*b, sep='\n')
if(b != 0):
    print('%.4f' % (a/b))
else: print('INVALID')