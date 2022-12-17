import random

print(random.randint(-2, 9))
print(random.randrange(-2, 9))

print(random.random())

c = random.uniform(-5, 5)
print(c)

random.seed(17)   # явно устанавливаем начальное значение для генератора случайных чисел

for _ in range(10):
    print(random.randint(1, 100))