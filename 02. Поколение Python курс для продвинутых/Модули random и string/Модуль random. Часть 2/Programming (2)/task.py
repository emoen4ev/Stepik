import random

matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

[random.shuffle(el) for el in matrix]
random.shuffle(matrix)

# print(*matrix)

# ----------------------------------------------------------------

# from random import shuffle
# from time import sleep
# from os import system
# from colorama import Fore
#
#
# def shuffle_rows():
#     global matrix
#     [shuffle(i) for i in matrix]
#
#
# def shuffle_flat():
#     global matrix
#     h, w, lst = len(matrix), len(matrix[0]), sum(matrix, [])
#     shuffle(lst)
#     matrix = [[lst[i * w + j] for j in range(w)] for i in range(h)]
#
#
# def print_2d_mtrx(matrix):
#     for row in matrix:
#         for el in row:
#             print(Fore.RED + el + Fore.RESET if el else el, end=' ')
#         print()
#
#
# matrix = [[0, 0, 0, 0],
#           [0, 0, 0, 0],
#           [0, 0, 0, 0],
#           [0, 0, 0, 'A']]
#
# for _ in range(50):
#     print("Перемешивать строки меж собой:")
#     shuffle_rows()
#     print_2d_mtrx(matrix)
#     sleep(.07)
#     system("cls")
#
# sleep(.2)
#
# for _ in range(50):
#     print("Перемешивать всю матрицу")
#     shuffle_flat()
#     print_2d_mtrx(matrix)
#     sleep(.07)
#     system("cls")