m = int(input())

result = set()

for i in range(m):
    n = int(input())
    current_set = {input() for _ in range(n)}
    if i == 0:
        result.update(current_set)
    else:
        result = result.intersection(current_set)

print(*sorted(result), sep='\n')