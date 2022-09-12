n = int(input())
counter = 0
for i in range(n):
    for j in range(i + 1):
        counter += 1
        print(counter, end=" ")
    print()