def pascal(number):
    triangle = []

    for i in range(number + 1):
        row = [1] * (i + 1)
        for j in range(i + 1):
            if j not in (0, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

    # for row in triangle:
    #     print(row)

    return triangle[number]


n = int(input())

print(pascal(n))