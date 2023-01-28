number_words = int(input())

data = [input() for _ in range(number_words)]

sorted_data = sorted(data, key=lambda x: (sum([ord(a.upper()) - ord('A') for a in x]), x))

print(*sorted_data, sep='\n')


# result = []
# for word in data:
#     summator = 0
#     for ch in word.upper():
#         summator += ord(ch) - ord('A')
#     result.append(summator)
#
# for i in range(len(data)):
#     print(f'{data[i]}: {result[i]}')