r_g_b = map(lambda x: 255 - x, [int(x) for x in input().split()])

print(*r_g_b)

# print(*map(lambda c: 255 - int(c), input().split()))