from string import ascii_letters, digits
from random import choices


def generate_password(length):
    return choices(base_sequence, k=length)


def generate_passwords(count, length):
    for _ in range(count):
        print(''.join(generate_password(length)))


n, m = int(input()), int(input())

base_sequence = list((set(ascii_letters) | set(digits)) - {'l', 'I', '1', 'o', 'O', '0'})

generate_passwords(n, m)