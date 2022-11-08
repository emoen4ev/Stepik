n = int(input())
k = int(input())

sequence = list(range(1, n + 1))
winner = []
counter = 1

if k != 1:
    while len(sequence) > 1:
        for i in range(len(sequence)):
            if counter % k != 0:
                winner.append(sequence[i])
                counter += 1
            else:
                counter = 1

        sequence = winner
        winner = []

print(sequence[-1])