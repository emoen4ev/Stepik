text = input()

vowels_letters = 0
consonants_letters = 0

for c in text:
    if c in "аАуУоОыЫиИэЭяЯюЮёЁеЕ":
        vowels_letters += 1
    if c in "бБвВгГдДжЖзЗйЙкКлЛмМнНпПрРсСтТфФхХцЦчЧшШщЩ":
        consonants_letters += 1

print(f"Количество гласных букв равно {vowels_letters}")
print(f"Количество согласных букв равно {consonants_letters}")
