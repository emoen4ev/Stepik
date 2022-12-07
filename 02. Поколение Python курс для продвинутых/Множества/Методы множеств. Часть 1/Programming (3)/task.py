numbers = [number.lstrip('0') for number in input().split()]

unique_numbers = set()

for number in numbers:
    print('YES' if number in unique_numbers else 'NO')
    unique_numbers.add(number)