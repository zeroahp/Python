c = ord(input()[0])

if c >= 97 and c <= 122 :
    print(chr(c).upper())
elif c >= 65 and c <= 90 :
    print(chr(c).lower())
else: print(chr(c))
