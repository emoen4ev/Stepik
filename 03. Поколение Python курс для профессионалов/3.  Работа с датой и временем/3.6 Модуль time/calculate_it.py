"""
Функция calculate_it()

Реализуйте функцию calculate_it(), которая принимает один или более аргументов в следующем порядке:
 - func — произвольная функция
 - *args — переменное количество позиционных аргументов, каждый из которых является произвольным объектом

Функция должна возвращать кортеж, первым элементом которого является возвращаемое значение функции func
при вызове с аргументами *args, а вторым — примерное время (в секундах), затраченное на вычисление этого значения.

Примечание 1. Например, если функция add() определена так:

def add(a, b, c):
    time.sleep(3)
    return a + b + c

то вызов:

calculate_it(add, 1, 2, 3)

должен вернуть кортеж (6, 3.000720262527466), где 6 — результат вызова add(1, 2, 3),
а 3.000720262527466 — примерное время работы функции add() в секундах.
"""

import time
from typing import Callable, Any


def calculate_it(func: Any, *args: Any) -> tuple[Any, float]:
    start = time.perf_counter()
    result = func(*args)
    end = time.perf_counter()
    elapsed_time = end - start

    return result, elapsed_time


# def add(*args: int) -> int:
#     result = 0
#     for el in args:
#         result += el
#         time.sleep(1)
#
#     return result
#
#
# print(calculate_it(add, 1, 2, 3))