"""
---------- task / requirements --------
Функция convert()

Реализуйте функцию convert(), которая принимает один аргумент:
- string — произвольная строка

Функция должна возвращать строку string:
- полностью в нижнем регистре, если букв в нижнем регистре в этой строке больше
- полностью в верхнем регистре, если букв в верхнем регистре в этой строке больше
- полностью в нижнем регистре, если количество букв в верхнем и нижнем регистрах в этой строке совпадает

Примечание 1. Символы строки, не являющиеся буквами, следует игнорировать.
"""


def convert(text: str) -> str:
    lowercase_counter = sum([x.islower() for x in text])
    uppercase_counter = sum([x.isupper() for x in text])

    return text.upper() if uppercase_counter > lowercase_counter else text.lower()


# ------- test inputs -----
print(convert('BEEgeek'))
print(convert('pyTHON'))
print(convert('pi31415!'))

'''
--------- expected outputs --------
beegeek
PYTHON
pi31415!
'''