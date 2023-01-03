from fractions import Fraction


num_1 = input()
num_2 = input()

print(f'{num_1} + {num_2} = {Fraction(num_1) + Fraction(num_2)}')
print(f'{num_1} - {num_2} = {Fraction(num_1) - Fraction(num_2)}')
print(f'{num_1} * {num_2} = {Fraction(num_1) * Fraction(num_2)}')
print(f'{num_1} / {num_2} = {Fraction(num_1) / Fraction(num_2)}')