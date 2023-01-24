rows_cols = int(input())

for _ in range(rows_cols):
    counter = 0

    current_row = [int(x) for x in input().split()]

    average = sum(current_row) / len(current_row)

    for el in current_row:
        if el > average:
            counter += 1

    print(counter)