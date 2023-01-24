n, m, k, x, y, z, t, all_students = [int(input()) for _ in range(8)]

a = m + n - x - t
b = n + k - z - t
c = m + k - y - t

one_book = (n - a - t - b) + (m - a - t - c) + (k - b - t - c)
two_books = a + b + c
zero_books = all_students - (one_book + two_books + t)

print(one_book)
print(two_books)
print(zero_books)