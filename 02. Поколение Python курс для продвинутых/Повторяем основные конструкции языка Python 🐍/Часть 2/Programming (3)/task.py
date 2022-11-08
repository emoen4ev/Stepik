initial_sequence = input().split()

result = [initial_sequence.pop()]

result.extend(initial_sequence)

print(*result)