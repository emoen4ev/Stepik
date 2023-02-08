"""
---------- task / requirements --------
Функция index_of_nearest()

Реализуйте функцию index_of_nearest(), которая принимает два аргумента в следующем порядке:
- numbers — список целых чисел
- number — целое число

Функция должна находить в списке numbers ближайшее по значению число к числу number и возвращать его индекс.
Если список numbers пуст, функция должна вернуть число -1.

Примечание 1. Если в функцию передается список, содержащий несколько чисел, одновременно являющихся ближайшими
к искомому числу, функция должна возвращать наименьший из индексов ближайших чисел.

Примечание 2. Рассмотрим третий тест. Ближайшими числами к числу 4 являются 5 и 3, имеющие индексы 1 и 2 соответственно.
Наименьший из индексов равен 1.
"""


def index_of_nearest(numbers: list, number: int) -> int:
    if not numbers:
        return -1

    min_diff = min(numbers, key=lambda current_number: abs(current_number - number))

    return numbers.index(min_diff)


# ------- test inputs -----
print(index_of_nearest([], 17))
print(index_of_nearest([7, 13, 3, 5, 18], 0))
print(index_of_nearest([9, 5, 3, 2, 11], 4))
print(index_of_nearest([7, 5, 4, 4, 3], 4))

'''
--------- expected outputs --------
-1
2
1
2
'''