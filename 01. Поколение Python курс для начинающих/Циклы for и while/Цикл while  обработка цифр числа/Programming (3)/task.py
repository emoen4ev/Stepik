n = int(input())

sum_of_digits = 0
number_of_digits = 0
product_of_digits = 1

last_digit_n = n % 10
n_initially = n

while n:
    last_digit = n % 10
    sum_of_digits += last_digit
    number_of_digits += 1
    product_of_digits *= last_digit
    n = n // 10

arithmetic_average_of_digits = sum_of_digits / number_of_digits
first_digit = n_initially // pow(10, (number_of_digits - 1))
sum_of_first_and_last_digit = first_digit + last_digit_n

print(sum_of_digits, number_of_digits, product_of_digits, arithmetic_average_of_digits, first_digit,
      sum_of_first_and_last_digit, sep="\n")