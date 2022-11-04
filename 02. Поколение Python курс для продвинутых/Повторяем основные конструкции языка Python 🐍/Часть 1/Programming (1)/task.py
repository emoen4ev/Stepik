m = float(input())
h = float(input())

opt_min = 18.5
opt_max = 25

body_mass_index = m / h ** 2

if body_mass_index < opt_min:
    print('Недостаточная масса')
elif body_mass_index > opt_max:
    print('Избыточная масса')
else:
    print('Оптимальная масса')