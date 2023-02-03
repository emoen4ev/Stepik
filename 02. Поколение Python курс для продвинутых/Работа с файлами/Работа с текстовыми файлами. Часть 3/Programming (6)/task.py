max_time_in_minutes = 59
output_data = []

with open('logfile.txt', 'rt', encoding='utf-8') as input_file:
    data = [el.strip().split(', ') for el in input_file]
    for current_data in data:
        name, start, end = current_data[0], [int(x) for x in current_data[1].split(':')], [int(x) for x in
                                                                                           current_data[2].split(':')]

        remaining_time = (end[0] * 60 + end[1]) - (start[0] * 60 + start[1])

        if remaining_time > max_time_in_minutes:
            output_data.append(name)

        # remaining_time > max_time_in_minutes and output_data.append(name)

result = '\n'.join(output_data)

with open('output.txt', 'wt', encoding='utf-8') as output_file:
    output_file.write(result)