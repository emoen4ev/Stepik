m = int(input())

n = int(input())

home_library_books = {input() for _ in range(m)}

book_list = [input() for _ in range(n)]

for book in book_list:
    print('YES' if book in home_library_books else 'NO')