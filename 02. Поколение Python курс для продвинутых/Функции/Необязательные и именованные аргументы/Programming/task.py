def matrix(n=1, m=None, value=0) -> list:
    if m is None:
        m = n
    return [[value] * m for _ in range(n)]


# print(matrix())
# print(matrix(3))
# print(matrix(2, 5))
# print(matrix(3, 4, 9))