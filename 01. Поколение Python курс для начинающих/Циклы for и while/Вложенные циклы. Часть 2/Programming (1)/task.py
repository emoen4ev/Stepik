n = int(input())

for i in range(1, n + 1):
    for j in range(1, 2 * i):
        if j < i + 1:
            print(j, end="")
        else:
            print(2 * i - j, end="")
    print()