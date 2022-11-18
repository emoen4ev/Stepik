# def chunked(text, number):
#     counter = 0
#     result = []
#     current = []
#
#     for el in text:
#         if counter < number:
#             current.append(el)
#             counter += 1
#         else:
#             result.append(current)
#             current = [el]
#             counter = 1
#
#     result.append(current)
#
#     return result
#
#
# sequence = input().split()
# n = int(input())
#
# print(chunked(sequence, n))

def chunked(symbols, n):
    result = []
    for i in range(0, len(symbols), n):
        result.append(symbols[i:i + n])
    return result


symbols = input().split()
n = int(input())

print(chunked(symbols, n))