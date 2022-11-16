number = int(input())

sequence = [input() for _ in range(number)]

initial = 'anton'
counter = 0
stop_counter = False

for word in sequence:
    ind = 0
    for ch in word:
        if ch == initial[ind]:
            counter += 1
            ind += 1
            if counter == len(initial):
                stop_counter = True

        if stop_counter:
            print(sequence.index(word) + 1, end=' ')
            counter = 0
            stop_counter = False
            break