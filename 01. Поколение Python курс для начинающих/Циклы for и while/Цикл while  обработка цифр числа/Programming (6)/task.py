n = int(input())

last_digit_initially = n % 10
increasing_numbers = True

while n:
    last_digit = n % 10
    if last_digit >= last_digit_initially:
        last_digit_initially = last_digit
        n //= 10
    else:
        increasing_numbers = False
        n = 0

if increasing_numbers:
    print("YES")
else:
    print("NO")


