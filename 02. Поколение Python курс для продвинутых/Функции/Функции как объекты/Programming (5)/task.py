def get_sum_digits(element):
    digits = list(map(int, element))
    return sum(digits)


sequence = list(input().split())

sequence.sort(key=get_sum_digits)

print(*sequence)