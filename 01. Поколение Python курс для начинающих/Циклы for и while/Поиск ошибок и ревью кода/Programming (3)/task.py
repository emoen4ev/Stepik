n = int(input())
max_digit = -1  # 1
while n > 0:
    digit = n % 10
    if digit % 3 == 0:
        if digit > max_digit:  # 2
            max_digit = digit  # 3
    n //= 10  # 4
if max_digit == -1:  # 5
    print('NO')
else:
    print(max_digit)
