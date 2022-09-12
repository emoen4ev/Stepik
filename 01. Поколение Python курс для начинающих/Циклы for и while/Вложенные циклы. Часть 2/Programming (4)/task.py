n = int(input())

sum_digits = 0

while n:
    sum_digits += n % 10
    n //= 10
    if n == 0:
        n = sum_digits
        if n <= 9:
            print(n)
            break
        sum_digits = 0