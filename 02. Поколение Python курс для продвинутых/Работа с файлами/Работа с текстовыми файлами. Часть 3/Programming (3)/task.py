with open('class_scores.txt', 'rt', encoding='utf-8') as input_file:
    data = {key: int(value) + min(5, 100 - int(value)) for key, value in [el.strip().split() for el in input_file]}

with open('new_scores.txt', 'w', encoding='utf-8') as output_file:
    for key, value in data.items():
        print(f'{key} {value}', file=output_file)

# with open('new_scores.txt', 'rt', encoding='utf-8') as file:
#     dd = file.readlines()
# print(dd)

''' ------------------------ class_scores.txt ------------------------
Гуев 100
Маргиев 99
Чаниев 95
Тепсикоев 94
Левитский 80
Габолаев 0
Хлюстова 10
Гергиева 85
'''