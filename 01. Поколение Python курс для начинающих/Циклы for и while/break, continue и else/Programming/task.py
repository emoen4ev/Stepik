n = int(input())
the_smallest_divisor = 0
for i in range(2, n + 1):
    if n % i == 0:
        the_smallest_divisor = i
        break
    else:
        i += 1
print(the_smallest_divisor)