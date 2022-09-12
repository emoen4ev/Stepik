counter_1 = 0
counter_2 = 0

text = input()
for c in text:
    if c == "+":
        counter_1 += 1
    if c == "*":
        counter_2 += 1
print(f"Символ + встречается {counter_1} раз")
print(f"Символ * встречается {counter_2} раз")