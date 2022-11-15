timur_ruslan = [input(), input()]

sequence = ['ножницы', 'бумага', 'камень', 'ящерица', 'Спок']

ind_diff = abs(sequence.index(timur_ruslan[0]) - sequence.index(timur_ruslan[1]))

winner = 'Руслан'

if timur_ruslan[0] == timur_ruslan[1]:
    winner = 'ничья'

elif ind_diff % 2 == 1:
    if sequence.index(timur_ruslan[0]) < sequence.index(timur_ruslan[1]):
        winner = 'Тимур'

elif ind_diff % 2 == 0:
    if sequence.index(timur_ruslan[0]) > sequence.index(timur_ruslan[1]):
        winner = 'Тимур'

print(winner)