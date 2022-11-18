n = int(input())

my_list = [[x for x in range(1, n + 1)] for _ in range(n)]

for row in my_list:
    print(row, end='\n')