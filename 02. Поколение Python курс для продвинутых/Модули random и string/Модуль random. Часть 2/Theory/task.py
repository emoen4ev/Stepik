import random

l = ['jj', 1, 5, False]

t = ('r', True, 4, 'fgh')

s = 'SDFGDH'

x = {2, 5, 'hgf'}

random.shuffle(l)

print(l)

ll = random.choice(l)
tt = random.choice(t)
ss = random.choice(s)


print(ll)
print(tt)
print(ss)

print(type(ll))
print(type(tt))
print(type(ss))