countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
capitals = ['Moscow', 'Washington', 'London', 'Berlin', 'Paris', 'Delhi']
population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]

data = zip(capitals, countries, population)

for cur_capital, cur_country, cur_population in data:
    print(f'{cur_capital} is the capital of {cur_country}, population equal {cur_population} people.')