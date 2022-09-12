# from math import factorial
#
# n = int(input())
# sum_factorials = 0
#
# while n:
#     sum_factorials += factorial(n)
#     n -= 1
#
# print(sum_factorials)


n = int(input())

factorial_n = 1
sum_factorials_n = 0

for i in range(1, n + 1):
    for j in range(1, i + 1):
        factorial_n *= j
    sum_factorials_n += factorial_n
    factorial_n = 1

print(sum_factorials_n)