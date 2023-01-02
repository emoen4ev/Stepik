from decimal import *


num = Decimal(input())

num_tuple = num.as_tuple()

num_digits = num_tuple.digits

if len(num_digits) == abs(num_tuple.exponent):
    num_digits += (0,)
# elif num_tuple.sign == 1:
#     num_digits = list(num_digits)
#     first_digit = num_digits.pop(0)
#     num_digits.append(-first_digit)

smallest_digit = min(num_digits)
largest_digit = max(num_digits)

result = smallest_digit + largest_digit

print(result)