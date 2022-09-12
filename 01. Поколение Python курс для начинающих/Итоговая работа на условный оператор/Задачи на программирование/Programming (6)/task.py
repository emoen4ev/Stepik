column_1, row_1, column_2, row_2 = int(input()), int(input()), int(input()), int(input())
if column_2 - column_1 == 1 and (row_2 - row_1 == 2 or row_1 - row_2 == 2):
    print("YES")
elif column_2 - column_1 == 2 and (row_2 - row_1 == 1 or row_1 - row_2 == 1):
    print("YES")
elif column_1 - column_2 == 1 and (row_2 - row_1 == 2 or row_1 - row_2 == 2):
    print("YES")
elif column_1 - column_2 == 2 and (row_2 - row_1 == 1 or row_1 - row_2 == 1):
    print("YES")
else:
    print("NO")