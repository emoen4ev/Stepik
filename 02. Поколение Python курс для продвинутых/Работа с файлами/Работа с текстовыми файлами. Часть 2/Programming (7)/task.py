with open('population.txt', 'rt', encoding='utf-8') as file:
    for line in file:
        name, population = line.strip().split('\t')
        if name.startswith('G') and int(population) > 500000:
            print(name)