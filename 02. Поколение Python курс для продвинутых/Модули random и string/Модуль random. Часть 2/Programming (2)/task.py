import random

matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

[random.shuffle(el) for el in matrix]
random.shuffle(matrix)

# print(*matrix)