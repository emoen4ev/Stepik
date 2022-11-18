# rows, cols = 3, 4                # rows - количество строк, cols - количество столбцов
#
# matrix  = [[277, -930, 11, 0],
#            [9, 43, 6, 87],
#            [4456, 8, 290, 7]]
#
# for r in range(rows):
#     for c in range(cols):
#         print(str(matrix[r][c]).ljust(6), end='')
#     print()

n = 5
a = [[19, 21, 33, 78, 99],
     [41, 53, 66, 98, 76],
     [79, 80, 90, 60, 20],
     [33, 11, 45, 67, 90],
     [45, 67, 12, 98, 23]]

maximum = -1
minimum = 100

for i in range(n):
    if a[i][i] > maximum:
        maximum = a[i][i]
    if a[i][n - i - 1] < minimum:
        minimum = a[i][n - i - 1]
print(minimum + maximum)