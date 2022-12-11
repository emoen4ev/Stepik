n = int(input())

result = set(input())

for _ in range(n - 1):
    current = set(input())
    result &= current

result = sorted(result)

print(*result)