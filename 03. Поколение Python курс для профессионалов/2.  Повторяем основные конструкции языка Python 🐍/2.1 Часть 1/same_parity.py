"""
-------- task / requirements ----------
Функция same_parity():

Реализуйте функцию same_parity(), которая принимает один аргумент: numbers — список целых чисел.

Функция должна возвращать новый список, элементами которого являются числа из списка numbers, имеющие ту же четность,
что и первый элемент этого списка.

Примечание 1. Числа в возвращаемом функцией списке должны располагаться в своем исходном порядке.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию same_parity(), но не код,
вызывающий ее.
"""


def same_parity(numbers: list) -> list:
    if numbers:
        parity = numbers[0] % 2
        return list(filter(lambda x: x % 2 == parity, numbers))
    return numbers

    # return [i for i in nums if i % 2 == nums[0] % 2]


# ------- test inputs -----
# print(same_parity([]))
# print(same_parity([6, 0, 67, -7, 10, -20]))
# print(same_parity([-7, 0, 67, -9, 70, -29, 90]))

'''
--------- expected outputs --------
[]
[6, 0, 10, -20]
[-7, 67, -9, -29]
'''