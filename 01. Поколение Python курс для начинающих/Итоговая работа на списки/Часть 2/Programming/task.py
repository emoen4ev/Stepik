n = int(input())

list_even_numbers = []

for number in range(2, n + 1):
    if number % 2 == 0:
        list_even_numbers.append(number)

print(list_even_numbers)
