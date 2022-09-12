from math import ceil

a, b = int(input()), int(input())

max_sum_of_divisors = 0
number_with_max_sum_of_divisors = 0

for i in range(a, b + 1):
    current_max_sum = i
    for j in range(1, ceil(i / 2) + 1):
        if i % j == 0:
            current_max_sum += j
        if current_max_sum >= max_sum_of_divisors:
            max_sum_of_divisors = current_max_sum
            number_with_max_sum_of_divisors = j * 2

print(number_with_max_sum_of_divisors, max_sum_of_divisors)
