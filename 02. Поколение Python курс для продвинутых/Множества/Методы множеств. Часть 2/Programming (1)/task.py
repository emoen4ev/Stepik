s_1, s_2 = set(input().split()), set(input().split())

s_3 = s_1.intersection(s_2)

result = sorted(int(_) for _ in s_3)

print(*result)