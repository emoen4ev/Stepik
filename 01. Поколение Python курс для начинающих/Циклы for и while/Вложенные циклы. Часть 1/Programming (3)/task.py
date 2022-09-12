n = int(input())
middle = ((n - 1) / 2) + 1
for i in range(1, n + 1):
    if i <= middle:
        for j in range(i):
            print("*", end="")
    else:
        for k in range((n + 1) - i):
            print("*", end="")
    print()