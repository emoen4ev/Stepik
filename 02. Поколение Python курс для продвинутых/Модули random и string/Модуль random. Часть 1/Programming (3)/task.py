from random import randint

password = set()

password_length = 7
min_limit = 1
max_limit = 49

while len(password) < password_length:
    new_digit = randint(min_limit, max_limit)
    password.add(new_digit)

password = sorted(password)

print(*password, end=' ')