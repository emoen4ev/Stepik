import random

n = int(input())

initial_set = [input() for _ in range(n)]

work_set_1, work_set_2 = initial_set.copy(), initial_set.copy()
random.shuffle(work_set_2)
counter = len(work_set_1)

while counter:
    for i in range(len(work_set_1)):
        if work_set_1[i] != work_set_2[i]:
            counter -= 1
        else:
            random.shuffle(work_set_2)
            counter = len(work_set_1)
            break

for i in range(len(work_set_1)):
    print(f'{work_set_1[i]} - {work_set_2[i]}')