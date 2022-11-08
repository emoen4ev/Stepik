sequence = list(map(int, input().split()))
for i in range(1, len(sequence), 2):
    sequence[i], sequence[i - 1] = sequence[i - 1], sequence[i]

print(*sequence)