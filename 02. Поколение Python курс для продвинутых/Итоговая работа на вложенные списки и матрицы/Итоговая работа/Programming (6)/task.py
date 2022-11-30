board_size = 8

col_q, row_q = input()

board = [['.'] * board_size for _ in range(board_size)]

row_q = board_size - int(row_q)
col_q = ord(col_q) - 97

for current_row in range(board_size):
    for current_col in range(board_size):
        if current_row == row_q or current_col == col_q:
            board[current_row][current_col] = '*'
        elif abs(current_row - row_q) == abs(current_col - col_q):
            board[current_row][current_col] = '*'

board[row_q][col_q] = 'Q'

for line in board:
    print(*line)