number = int(input())

sequence = [input() for _ in range(number)]

initial = 'anton'

for word in sequence:
    ind = 0
    for ch in word:
        if ch == initial[ind]:
            pass