"""
Функция get_the_fastest_func()

Реализуйте функцию get_the_fastest_func(), которая принимает два аргумента в следующем порядке:
 - funcs — список произвольных функций
 - arg — произвольный объект

Функция get_the_fastest_func() должна возвращать функцию из списка funcs,
которая затратила на вычисление значения при вызове с аргументом arg наименьшее количество времени.
"""

from time import perf_counter, sleep
from typing import Any, Callable


def get_the_fastest_func(funcs: list, arg: Any) -> Callable:
    least_time = float('inf')
    fastest_function = None

    for func in funcs:
        start = perf_counter()
        func(arg)
        end = perf_counter()
        elapsed_time = end - start
        if elapsed_time < least_time:
            fastest_function = func
            least_time = elapsed_time

    return fastest_function


# def slow(arg):
#     sleep(3)
#
#
# def mid(arg):
#     sleep(2)
#
#
# def fast(arg):
#     sleep(1)
#
#
# funcs = [slow, mid, fast]
#
# print(get_the_fastest_func(funcs, 6))