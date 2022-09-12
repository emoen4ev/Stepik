a, b = int(input()), int(input())

if a == 1:
    a = 2

for i in range(a, b + 1):
    k = True
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            k = False
            break
    if k:
        print(i)
