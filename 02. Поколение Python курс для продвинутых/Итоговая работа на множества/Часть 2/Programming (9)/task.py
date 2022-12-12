m, n = int(input()), int(input())

set_m = {input() for _ in range(m)}
set_n = {input() for _ in range(n)}

result = len(set_m.symmetric_difference(set_n))

print(result if result else 'NO')