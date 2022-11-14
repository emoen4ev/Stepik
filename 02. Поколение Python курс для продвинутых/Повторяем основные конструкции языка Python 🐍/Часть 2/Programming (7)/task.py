tr = [input(), input()]
print(tr)

sequence = ['ножницы', 'бумага', 'камень', 'ящерица', 'Спок']

if tr[0] == tr[1]:
    winner = 'ничья'
elif abs(sequence.index(tr[0]) - sequence.index(tr[1])) == 1:
    pass
elif abs(sequence.index(tr[0]) - sequence.index(tr[1])) == sequence.index(tr[-1]):
    pass
elif abs(sequence.index(tr[0]) - sequence.index(tr[1])) == 2:
    pass

print(sequence.index(tr[0]))