sequence = input().split()
counter = 1

for i in range(len(sequence) - 1):
    if sequence[i + 1] != sequence[i]:
        counter += 1

print(counter)