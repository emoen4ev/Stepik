sequence = input()

sequence_s = set(sequence)

print('YES' if len(sequence) == len(sequence_s) else 'NO')