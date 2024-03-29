"""
---------- task / requirements --------
Функция print_given():

Реализуйте функцию print_given(), которая принимает произвольное количество позиционных и именованных аргументов
и выводит все переданные аргументы, указывая тип каждого.
Пары аргумент-тип должны выводиться каждая на отдельной строке, в следующем формате:
- для позиционных аргументов: <значение аргумента> <тип аргумента>
- для именованных аргументов: <имя переменной> <значение аргумента> <тип аргумента>

Примечание 1. При выводе позиционные аргументы должны быть расположены в порядке их передачи,
              именованные — в лексикографическом порядке имен переменных.

Примечание 2. При выводе сначала должны следовать все позиционные аргументы, затем — все именованные.

Примечание 3. Если в функцию ничего не передается, функция ничего не должна выводить.
"""
from typing import Any


def print_given(*args: Any, **kwargs: Any) -> None:

    print(*[f'{el} {type(el)}' for el in args], sep='\n')
    print(*[f'{key} {value} {type(value)}' for key, value in sorted(kwargs.items())], sep='\n')

    # [print(el, type(el)) for el in args]
    # [print(key, value, type(value)) for key, value in sorted(kwargs.items())]

    # for el in args:
    #     print(el, type(el))
    # for key, value in sorted(kwargs.items()):
    #     print(key, value, type(value))


# ------- test inputs -----
print_given(1, [1, 2, 3], 'three', two=2)
print_given('apple', 'cherry', 'watermelon')
print_given(b=2, d=4, c=3, a=1)
print_given()

'''
--------- expected outputs --------
1 <class 'int'>
[1, 2, 3] <class 'list'>
three <class 'str'>
two 2 <class 'int'>

apple <class 'str'>
cherry <class 'str'>
watermelon <class 'str'>

a 1 <class 'int'>
b 2 <class 'int'>
c 3 <class 'int'>
d 4 <class 'int'>



'''