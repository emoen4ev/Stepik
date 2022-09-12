# объявление функции
def print_fio(p_name, p_surname, p_patronymic):
  # print(p_surname[0].capitalize(), p_name[0].capitalize(), p_patronymic[0].capitalize(), sep='')
    print((p_surname[0] + p_name[0] + p_patronymic[0]).upper())


# считываем данные
name, surname, patronymic = input(), input(), input()

# вызываем функцию
print_fio(name, surname, patronymic)
