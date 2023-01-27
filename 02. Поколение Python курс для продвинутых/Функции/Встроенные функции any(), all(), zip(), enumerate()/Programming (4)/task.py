def divisible_by_digits(a, b):
    result = []
    for i in range(a, b + 1):
        if '0' in str(i):
            continue
        digits = [int(d) for d in str(i)]
        if all(i % d == 0 for d in digits):
            result.append(i)
    return result


# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
print(*divisible_by_digits(int(input()), int(input())))