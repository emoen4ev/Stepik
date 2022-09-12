column_1, row_1, column_2, row_2 = int(input()), int(input()), int(input()), int(input())
if column_1 - row_1 == column_2 - row_2 or column_1 + row_1 == column_2 + row_2:
    print("YES")
else:
    print("NO")
