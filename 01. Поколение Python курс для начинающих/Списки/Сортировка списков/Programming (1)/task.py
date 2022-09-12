a = [78, -32, 5, 39, 58, -5, -63, 57, 72, 9, 53, -1, 63, -97, -21, -94, -47, 57, -8, 60, -23, -72, -22, -79, 90, 96, -41, -71, -48, 84, 89, -96, 41, -16, 94, -60, -64, -39, 60, -14, -62, -19, -3, 32, 98, 14, 43, 3, -56, 71, -71, -67, 80, 27, 92, 92, -64, 0, -77, 2, -26, 41, 3, -31, 48, 39, 20, -30, 35, 32, -58, 2, 63, 64, 66, 62, 82, -62, 9, -52, 35, -61, 87, 78, 93, -42, 87, -72, -10, -36, 61, -16, 59, 59, 22, -24, -67, 76, -94, 59]

n = len(a)

# for number in range(n - 1):
#     index_current_min = number
#     for number_unsorted in range(number, n):
#         if a[index_current_min] > a[number_unsorted]:
#             index_current_min = number_unsorted
#
#     a[number], a[index_current_min] = a[index_current_min], a[number]
#
# print(a)


i = 0
while i < n - 1:
    m = i
    j = i + 1
    while j < n:
        if a[j] < a[m]:
            m = j
        j += 1
    a[i], a[m] = a[m], a[i]
    i += 1

print(a)
