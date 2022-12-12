m = int(input())
n = int(input())

math_set = {input() for _ in range(m)}
info_set = {input() for _ in range(n)}

math_and_info = math_set.intersection(info_set)

only_math = math_set.difference(math_and_info)
only_info = info_set.difference(math_and_info)

result = len(only_math) + len(only_info)

print(result if result else 'NO')