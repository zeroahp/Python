a,b,c,d = map(float, input().split())

r = a + b + (c*2) + (d*3)
if r/7 >= 8 :
    print('GIOI')
elif r/7 < 8  and r/7 >6.5:
    print('KHA')
elif r/7 < 6.5 and r/7 >= 5 :
    print('TRUNG BINH')
else: print("YEU")