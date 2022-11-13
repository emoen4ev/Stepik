numbers = int(input())
sequence = []
result = 'НЕТ'

for _ in range(numbers):
    sequence.append(int(input()))

target = int(input())

if target == 0 and 0 in sequence:
    result = 'ДА'
else:
    for ind, value in enumerate(sequence):
        if value != 0 and target % value == 0:
            for _, value_1 in enumerate(sequence[ind + 1:]):
                if value * value_1 == target:
                    result = 'ДА'
                    break
        if result == 'ДА':
            break

print(result)