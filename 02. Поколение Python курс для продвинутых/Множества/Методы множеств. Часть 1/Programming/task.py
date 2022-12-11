n = int(input())

result = tuple()

for _ in range(n):
    current = set(input().lower())
    result += current,

for el in result:
    print(len(el))