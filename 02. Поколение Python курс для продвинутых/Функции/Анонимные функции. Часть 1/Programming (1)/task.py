from functools import reduce

data = [
    ['Tokyo', 35676000, 'primary'],
    ['New York', 19354922, 'nan'],
    ['Mexico City', 19028000, 'primary'],
    ['Mumbai', 18978000, 'admin'],
    ['Sao Paulo', 18845000, 'admin'],
    ['Delhi', 15926000, 'admin'],
    ['Shanghai', 14987000, 'admin'],
    ['Kolkata', 14787000, 'admin'],
    ['Los Angeles', 12815475, 'nan'],
    ['Dhaka', 12797394, 'primary'],
    ['Buenos Aires', 12795000, 'primary'],
    ['Karachi', 12130000, 'admin'],
    ['Cairo', 11893000, 'primary'],
    ['Rio de Janeiro', 11748000, 'admin'],
    ['Osaka', 11294000, 'admin'],
    ['Beijing', 11106000, 'primary'],
    ['Manila', 11100000, 'primary'],
    ['Moscow', 10452000, 'primary'],
    ['Istanbul', 10061000, 'admin'],
    ['Paris', 9904000, 'primary'],
]

# filter out cities with 'primary' in the 3rd column and population greater than 10000000
filtered_data = filter(lambda x: x[2] == 'primary' and x[1] > 10000000, data)

# extract the names of the cities from the filtered data
city_names = map(lambda x: x[0], filtered_data)

# sort the city names in alphabetical order
sorted_city_names = sorted(city_names)

# join the city names into a single string
result = reduce(lambda s, x: s + ', ' + x, sorted_city_names)

print('Cities: ' + result)