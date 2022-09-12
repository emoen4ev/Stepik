n = int(input())  # 1
product = 1  # 2
while n > 0:  # 3
    digit = n % 10
    product *= digit  # 4
    n //= 10
print(product)