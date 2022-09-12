n = int(input())

smallest_digit = n % 10
largest_digit = 0

while n:
    last_digit = n % 10
    if last_digit > largest_digit:
        largest_digit = last_digit
    elif last_digit < smallest_digit:
        smallest_digit = last_digit
    n //= 10
    
print(f"Максимальная цифра равна {largest_digit}\nМинимальная цифра равна {smallest_digit}")