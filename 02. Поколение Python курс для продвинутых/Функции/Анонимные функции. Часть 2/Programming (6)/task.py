data = [
    (19542209, 'New York'), (4887871, 'Alabama'), (1420491, 'Hawaii'), (626299, 'Vermont'), (1805832, 'West Virginia'),
    (39865590, 'California'), (11799448, 'Ohio'), (10711908, 'Georgia'), (10077331, 'Michigan'), (10439388, 'Virginia'),
    (7705281, 'Washington'), (7151502, 'Arizona'), (7029917, 'Massachusetts'), (6910840, 'Tennessee'),
]

sorted_data = sorted(data, key=lambda current_data: current_data[1][-1], reverse=True)

for population, city in sorted_data:
    print(f'{city}: {population}')