n = int(input())

n_initially = n
number_of_digits = 0

while n:
    number_of_digits += 1
    n = n // 10

first_two_digits_of_n_initially = n_initially // (pow(10, (number_of_digits - 2)))
the_second_digit = first_two_digits_of_n_initially % 10

print(the_second_digit)