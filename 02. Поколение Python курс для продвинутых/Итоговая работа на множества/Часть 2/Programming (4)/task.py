set_1 = {int(_) for _ in input().split()}
set_2 = {int(_) for _ in input().split()}

set_3 = set_1.intersection(set_2)

if set_3:
    print(*sorted(set_3, reverse=True))
else:
    print('BAD DAY')