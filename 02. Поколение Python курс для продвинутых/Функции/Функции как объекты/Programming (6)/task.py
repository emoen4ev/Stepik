def get_sum_digits(element: str) -> tuple:  # -> tuple[int, int]
    return sum(map(int, element)), int(element)


sequence = input().split()

sequence.sort(key=get_sum_digits)

print(*sequence)