n = int(input())
m = 0  # 1
while n > 0:
    m = n  # 2
    n //= 10  # 3
print(m)  # 4