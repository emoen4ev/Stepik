set_1 = {_ for _ in input().split()}
set_2 = {_ for _ in input().split()}

set_3 = set_1.union(set_2)

print(*sorted(set_3))