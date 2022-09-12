a, b, c = input(), input(), input()

if len(a) < len(b):
    a, b = b, a
if len(c) < len(b):
    c, b = b, c
if len(a) < len(c):
    a, c = c, a

print(b, a, sep='\n')




