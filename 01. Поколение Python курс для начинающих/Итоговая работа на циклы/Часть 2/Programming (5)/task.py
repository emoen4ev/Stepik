n = int(input())

number_of_digit_3 = 0
number_of_last_digit = 1
number_of_even_digits = 0
sum_of_digits_greater_than_5 = 0
product_of_digits_greater_than_7 = 1
how_many_times_digits_0_and_5_occur = 0

last_digit_initially = n % 10

while n > 0:
    last_digit_curr = n % 10
    if last_digit_curr == 3:
        number_of_digit_3 += 1
    if last_digit_curr % 2 == 0:
        number_of_even_digits += 1
    if last_digit_curr > 5:
        sum_of_digits_greater_than_5 += last_digit_curr
    if last_digit_curr > 7:
        product_of_digits_greater_than_7 *= last_digit_curr
    if last_digit_curr == 0 or last_digit_curr == 5:
        how_many_times_digits_0_and_5_occur += 1
    n //= 10
    last_digit_sec = n % 10
    if last_digit_sec == last_digit_initially:
        number_of_last_digit += 1
print(number_of_digit_3, number_of_last_digit, number_of_even_digits, sum_of_digits_greater_than_5,
      product_of_digits_greater_than_7, how_many_times_digits_0_and_5_occur, sep="\n")

