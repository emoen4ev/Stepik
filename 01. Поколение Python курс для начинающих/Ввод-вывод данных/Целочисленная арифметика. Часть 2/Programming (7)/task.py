number = int(input())
c = number % 10
b = (number // 10) % 10
a = number // 100
print(a, b, c, sep="")
print(a, c, b, sep="")
print(b, a, c, sep="")
print(b, c, a, sep="")
print(c, a, b, sep="")
print(c, b, a, sep="")




