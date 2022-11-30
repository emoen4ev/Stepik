board_size = 8

col_Q, row_Q = input()

board = [['.'] * board_size for _ in range(board_size)]

col_Q = ord(col_Q) - 97
row_Q = board_size - int(row_Q)

board[row_Q][col_Q] = 'Q'

for current_row in range(board_size):
    for current_col in range(board_size):
        if 0 <= current_row <= board_size and 0 <= current_col <= board_size and board[current_row][current_col] != 'Q':
            if current_row == row_Q:
                board[current_row][current_col] = '*'
            if current_col == col_Q:
                board[current_row][current_col] = '*'
            if abs(current_row - row_Q) == abs(current_col - col_Q):
                board[current_row][current_col] = '*'

for line in board:
    print(*line)