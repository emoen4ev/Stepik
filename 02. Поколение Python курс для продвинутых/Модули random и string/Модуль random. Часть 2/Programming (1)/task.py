from string import ascii_uppercase as uc
from random import randint as rt, sample as sm


def generate_index():
    return f'{"".join(sm(uc, 2))}{rt(0, 99)}_{rt(0, 99)}{"".join(sm(uc, 2))}'


# print(generate_index())