from random import randint

password = set()

password_length = 7

while len(password) < password_length:
    new_digit = randint(1, 49)
    password.add(new_digit)

password = sorted(password)

print(*password, end=' ')