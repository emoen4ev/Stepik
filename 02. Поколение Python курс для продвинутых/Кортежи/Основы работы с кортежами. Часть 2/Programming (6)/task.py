n = int(input())

p_1, p_2, p_3 = 1, 1, 1

for _ in range(n):
    print(p_1, end=' ')
    p_1, p_2, p_3 = p_2, p_3, p_1 + p_2 + p_3