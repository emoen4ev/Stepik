def pascal(number):
    triangle = []

    for i in range(number):
        row = [1] * (i + 1)
        for j in range(i + 1):
            if j not in (0, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)
        print(*row, end='\n')


n = int(input())

pascal(n)