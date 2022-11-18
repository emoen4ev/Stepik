n = int(input())

#  -------------------------------------------------------------

# my_list = []
#
# numbers = [int(x) for x in range(1, n + 1)]
#
# for number in numbers:
#     current_list = [x for x in range(1, number + 1)]
#     my_list.append(current_list)
#
# for row in my_list:
#     print(row, end='\n')

#  ---------------------------------------------------------------

my_list = [[x for x in range(1, y + 1)] for y in range(1, n + 1)]

print(*my_list, sep='\n')