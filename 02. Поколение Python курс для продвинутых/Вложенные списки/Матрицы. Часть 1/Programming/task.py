n, m = int(input()), int(input())

matrix = []

for _ in range(n):
    row = [input() for _ in range(m)]
    # row = []
    # for _ in range(m):
    #     row.append(input())
    matrix.append(row)

for row in matrix:
    print(*row)