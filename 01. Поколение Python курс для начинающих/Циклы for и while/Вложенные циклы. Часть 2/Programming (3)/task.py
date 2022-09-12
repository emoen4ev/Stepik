from math import ceil

n = int(input())
for i in range(1, n + 1):
    counter = 1
    for j in range(1, ceil(i / 2) + 1):
        if i % j == 0:
            if i > 1:
                counter += 1
    print(i, "+" * counter, sep="")