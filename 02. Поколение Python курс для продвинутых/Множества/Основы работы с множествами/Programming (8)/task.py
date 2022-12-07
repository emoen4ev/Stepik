text = input().split()

print('YES' if set(text[0]) == set(text[1]) == set(text[2]) else 'NO')