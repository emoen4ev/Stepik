n = int(input())

data = {}

for _ in range(n):
    cur_num, cur_name = input().lower().split()

    data.setdefault(cur_name, []).append(cur_num)

m = int(input())

for _ in range(m):
    name = input().lower()
    print(*data.get(name, ['абонент не найден']))