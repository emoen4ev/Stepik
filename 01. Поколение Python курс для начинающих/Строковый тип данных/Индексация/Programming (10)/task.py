n = int(input())

inverted_number = str(n % 2)

while n > 1:
    n //= 2
    inverted_number += str(n % 2)

number = inverted_number[len(inverted_number) - 1]

for i in range(len(inverted_number) - 1, 0, -1):
    number += inverted_number[i - 1]

print(number)
