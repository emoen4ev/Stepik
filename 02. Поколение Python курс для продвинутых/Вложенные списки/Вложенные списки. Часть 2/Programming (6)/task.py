sequence = input().split()

result = [[]]
current = []

for i in range(1, len(sequence) + 1):
    for j in range((len(sequence) + 1) - i):
        current = sequence[j:(j + i)]
        result.append(current)

print(result)