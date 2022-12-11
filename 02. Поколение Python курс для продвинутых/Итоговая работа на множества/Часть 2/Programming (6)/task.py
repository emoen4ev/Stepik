m = int(input())
n = int(input())

math_set = {input() for _ in range(m)}
info_set = {input() for _ in range(n)}

only_math = math_set.difference(info_set)

print(len(only_math))