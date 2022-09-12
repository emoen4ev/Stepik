count = 0
p = 1  # 1
for i in range(1, 11):  # 2
    x = int(input())
    if x >= 0:  # 3
        p *= x  # 4
        count += 1  # 5
if count > 0:
    print(count)  # 6
    print(p)
else:
    print('NO')
