from math import sqrt, pow

a = int(input())
b = int(input())

results = {

    'x_1': (a + b),
    'x_2': (a - b),
    'x_3': (a * b),
    'x_4': (a / b),
    'x_5': (a // b),
    'x_6': (a % b),
    'x_7': sqrt(pow(a, 10) + pow(b, 10)),

}

for key in results:
    print(results[key], end='\n')