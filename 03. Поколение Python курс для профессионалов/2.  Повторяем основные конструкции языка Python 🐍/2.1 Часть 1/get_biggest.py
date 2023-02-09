"""
---------- task / requirements --------
Функция get_biggest()

Реализуйте функцию get_biggest(), которая принимает один аргумент:
- numbers — список целых неотрицательных чисел

Функция должна возвращать наибольшее число, которое можно составить из чисел из списка numbers.
Если список numbers пуст, функция должна вернуть число −1.

Примечание 1. Рассмотрим первый тест со списком чисел [1, 2, 3], из которых можно составить следующие числа:
123, 132, 213, 231, 312, 321

Наибольшим из представленных является 321.
"""


def get_biggest(numbers: list) -> int:
    if not numbers:
        return -1

    sorted_numbers = sorted(map(str, numbers), key=lambda x: x * 4, reverse=True)

    return int(''.join(sorted_numbers))


# ------- test inputs -----
print(get_biggest([1, 2, 3]))
print(get_biggest([61, 228, 9, 3, 11]))
print(get_biggest([7, 71, 72]))
print(get_biggest([]))
print(get_biggest([7, 71, 72, 8]))
'''
--------- expected outputs --------
321
961322811
77271
-1
877271
'''