n = int(input())
last_digit = 0
while n > 99:
    last_digit = n % 10
    n //= 10
print(last_digit)
