number_words = int(input())

data = [input() for _ in range(number_words)]

sorted_data = sorted(data, key=lambda x: (sum([ord(a.upper()) - ord('A') for a in x]), x))

print(*sorted_data, sep='\n')