from math import log

n = int(input())
s = 1
for i in range(2, n + 1):
    s += 1 / i
ss = s - log(n)
print(ss)