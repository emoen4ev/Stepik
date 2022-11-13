t = input()
r = input()

if t == r:
    winner = 'ничья'
elif (t == 'ножницы' and r == 'бумага') or \
        (t == 'бумага' and r == 'камень') or \
        (t == 'камень' and r == 'ножницы'):
    winner = 'Тимур'
else:
    winner = 'Руслан'

print(winner)