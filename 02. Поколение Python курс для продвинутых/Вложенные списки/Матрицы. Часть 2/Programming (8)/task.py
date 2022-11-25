rows_cols = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(rows_cols)]

is_magic = True
used_values = []
initial_sum = sum(matrix[0])
sum_primary_diagonal = 0
sum_secondary_diagonal = 0

while True:
    for row in matrix:

        if sum(row) != initial_sum:
            is_magic = False
            break

    for col in range(rows_cols):
        col_sum = 0
        for row in range(rows_cols):

            if matrix[row][col] in used_values or matrix[row][col] == 0:
                is_magic = False
                break
            else:
                used_values.append(matrix[row][col])

            col_sum += matrix[row][col]

            if row == col:
                sum_primary_diagonal += matrix[row][col]
            if row == rows_cols - col - 1:
                sum_secondary_diagonal += matrix[row][col]

        if col_sum != initial_sum:
            is_magic = False
            break

    if sum_primary_diagonal != initial_sum or sum_secondary_diagonal != initial_sum:
        is_magic = False
        break
    break

print('YES' if is_magic else 'NO')