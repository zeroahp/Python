from math import *
c = input()[0]

if( c == "z" or c == "Z"):
    print("a")
else:
    c = ord(c) +1
    print(chr(c).lower())



