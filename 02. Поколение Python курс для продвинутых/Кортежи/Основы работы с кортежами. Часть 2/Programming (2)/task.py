poet_data = ('Пушкин', 1799, 'Санкт-Петербург')

poet_data_l = list(poet_data)

poet_data_l[2] = 'Москва'

poet_data = tuple(poet_data_l)

print(poet_data)