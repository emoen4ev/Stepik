first_line = input()

numbers_of_rows = int(first_line[1:])

for row in range(numbers_of_rows):
    new_row = input()
    if '#' in new_row:
        index_grid = new_row.index('#')
        print(new_row[:index_grid].rstrip())
    else:
        print(new_row.rstrip())
