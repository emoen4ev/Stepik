# def get_sum_digits(element):
#     return sum(map(int, element))
#
#
# sequence = input().split()
#
# sequence.sort(key=get_sum_digits)
#
# print(*sequence)

# ------------------------ Recursive Approach ------------------------

def get_sum_digits(element: int) -> int:
    return 0 if element == 0 else element % 10 + get_sum_digits(element // 10)


sequence = list(map(int, input().split()))

sequence.sort(key=get_sum_digits)

print(*sequence)