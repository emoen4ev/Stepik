n = int(input())

equality_of_digits = True
last_digit_initially = n % 10
last_digit = last_digit_initially

while n:
    last_digit = n % 10
    if last_digit != last_digit_initially:
        equality_of_digits = False
        n = 0
    n //= 10

if equality_of_digits:
    print("YES")
else:
    print("NO")