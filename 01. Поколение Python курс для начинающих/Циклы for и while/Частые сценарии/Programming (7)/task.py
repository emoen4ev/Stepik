n = int(input())
total = 0
for i in range(n):
    if i % 2 == 0:
        total += (i + 1)
    else:
        total -= (i + 1)
print(total)