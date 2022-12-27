from string import ascii_uppercase, ascii_lowercase, digits
from random import choice, choices, shuffle


def generate_password(length):
    psw = [choice(uppercase_set), choice(lowercase_set), choice(digits_set)]
    psw.extend(choices(base_sequence, k=(length - 3)))
    shuffle(psw)
    return ''.join(psw)


def generate_passwords(count, length):
    return [generate_password(length) for _ in range(count)]


n, m = int(input()), int(input())

uppercase_set = list(set(ascii_uppercase) - {'O', 'I'})
lowercase_set = list(set(ascii_lowercase) - {'l', 'o'})
digits_set = list(set(digits) - {'1', '0'})
base_sequence = uppercase_set + lowercase_set + digits_set

print(*generate_passwords(n, m), sep='\n')