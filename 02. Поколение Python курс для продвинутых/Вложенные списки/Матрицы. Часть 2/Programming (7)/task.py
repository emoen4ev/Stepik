board = [['.'] * 8 for _ in range(8)]

horse_coordinates = input()
horse_row = 8 - int(horse_coordinates[1])
horse_col = horse_coordinates[0]

horse_col_digit = 0

map_table = [
    ['a', 0],
    ['b', 1],
    ['c', 2],
    ['d', 3],
    ['e', 4],
    ['f', 5],
    ['g', 6],
    ['h', 7],
]

for el in map_table:
    if el[0] == horse_col:
        horse_col_digit = el[1]
        break

board[horse_row][horse_col_digit] = 'N'

if horse_row - 2 >= 0:
    if horse_col_digit - 1 >= 0:
        board[horse_row - 2][horse_col_digit - 1] = '*'
    if horse_col_digit + 1 <= 7:
        board[horse_row - 2][horse_col_digit + 1] = '*'
if horse_row - 1 >= 0:
    if horse_col_digit - 2 >= 0:
        board[horse_row - 1][horse_col_digit - 2] = '*'
    if horse_col_digit + 2 <= 7:
        board[horse_row - 1][horse_col_digit + 2] = '*'
if horse_row + 2 <= 7:
    if horse_col_digit - 1 >= 0:
        board[horse_row + 2][horse_col_digit - 1] = '*'
    if horse_col_digit + 1 <= 7:
        board[horse_row + 2][horse_col_digit + 1] = '*'
if horse_row + 1 <= 7:
    if horse_col_digit - 2 >= 0:
        board[horse_row + 1][horse_col_digit - 2] = '*'
    if horse_col_digit + 2 <= 7:
        board[horse_row + 1][horse_col_digit + 2] = '*'

for row in board:
    print(' '.join(str(x) for x in row))