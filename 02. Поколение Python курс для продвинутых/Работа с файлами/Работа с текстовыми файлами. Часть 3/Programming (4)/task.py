with open('goats.txt', 'rt', encoding='utf-8') as input_file:
    data = [el.strip() for el in input_file.readlines()]

    goats_idx = data.index('GOATS')

    colors_data = data[1:goats_idx]
    second_part = data[goats_idx + 1:]

    goats_data = sorted(filter(lambda x: x in colors_data, second_part))

    number_goats_by_colors = {key: goats_data.count(key) for key in goats_data}

with open('answer.txt', 'wt', encoding='utf-8') as output_file:
    for color, number in number_goats_by_colors.items():
        if number > len(goats_data) * 0.07:
            output_file.write(f'{color}\n')