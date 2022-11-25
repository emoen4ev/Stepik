fields = 8
board = [['.'] * fields for _ in range(fields)]

horse_coordinates = input()
horse_row = fields - int(horse_coordinates[1])
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

upper_board_limit = left_board_limit = 0
lower_board_limit = right_board_limit = fields - 1

if horse_row - 2 >= upper_board_limit:
    if horse_col_digit - 1 >= left_board_limit:
        board[horse_row - 2][horse_col_digit - 1] = '*'
    if horse_col_digit + 1 <= right_board_limit:
        board[horse_row - 2][horse_col_digit + 1] = '*'
if horse_row - 1 >= upper_board_limit:
    if horse_col_digit - 2 >= left_board_limit:
        board[horse_row - 1][horse_col_digit - 2] = '*'
    if horse_col_digit + 2 <= right_board_limit:
        board[horse_row - 1][horse_col_digit + 2] = '*'
if horse_row + 2 <= lower_board_limit:
    if horse_col_digit - 1 >= left_board_limit:
        board[horse_row + 2][horse_col_digit - 1] = '*'
    if horse_col_digit + 1 <= right_board_limit:
        board[horse_row + 2][horse_col_digit + 1] = '*'
if horse_row + 1 <= lower_board_limit:
    if horse_col_digit - 2 >= left_board_limit:
        board[horse_row + 1][horse_col_digit - 2] = '*'
    if horse_col_digit + 2 <= right_board_limit:
        board[horse_row + 1][horse_col_digit + 2] = '*'

for row in board:
    print(' '.join(str(x) for x in row))