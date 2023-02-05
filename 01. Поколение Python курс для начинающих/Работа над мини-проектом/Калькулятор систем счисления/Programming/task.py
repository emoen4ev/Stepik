number = int(input())

b = bin(number)[2:]
o = oct(number)[2:]
h = hex(number)[2:].upper()

print(b, o, h, sep='\n')