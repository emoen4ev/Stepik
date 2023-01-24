n = int(input())

data_set = {input() for _ in range(n)}

new_name = input()

print('OK' if new_name not in data_set else 'REPEAT')