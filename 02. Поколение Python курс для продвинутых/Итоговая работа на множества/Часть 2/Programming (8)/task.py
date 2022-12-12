set_1 = set(input().split())
set_2 = set(input().split())

set_3 = set_1.union(set_2)

print(*sorted(set_3))