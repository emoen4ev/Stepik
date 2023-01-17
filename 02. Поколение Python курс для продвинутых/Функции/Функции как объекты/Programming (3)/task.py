# def sort_by_name(cur_data: tuple) -> str:
#     return cur_data[0]
#
#
# def sort_by_age(cur_data: tuple) -> int:
#     return cur_data[1]
#
#
# def sort_by_height(cur_data: tuple) -> int:
#     return cur_data[2]
#
#
# def sort_by_weight(cur_data: tuple) -> int:
#     return cur_data[3]
#
#
# athletes = [
#     ('Дима', 10, 130, 35),
#     ('Тимур', 11, 135, 39),
#     ('Руслан', 9, 140, 33),
#     ('Рустам', 10, 128, 30),
#     ('Амир', 16, 170, 70),
#     ('Рома', 16, 188, 100),
#     ('Матвей', 17, 168, 68),
#     ('Петя', 15, 190, 90),
# ]
#
# sorting_type = int(input()) - 1
#
# types = [sort_by_name, sort_by_age, sort_by_height, sort_by_weight]
#
# athletes.sort(key=types[sorting_type])
#
# for athlete in athletes:
#     print(*athlete)


def sort_by_type(sort_type: int) -> str or int:
    def sorting(current_athlete: tuple):
        return current_athlete[sort_type]
    return sorting


athletes = [
    ('Дима', 10, 130, 35),
    ('Тимур', 11, 135, 39),
    ('Руслан', 9, 140, 33),
    ('Рустам', 10, 128, 30),
    ('Амир', 16, 170, 70),
    ('Рома', 16, 188, 100),
    ('Матвей', 17, 168, 68),
    ('Петя', 15, 190, 90),
]

sorting_type = int(input()) - 1

athletes.sort(key=sort_by_type(sorting_type))

[print(*current_athlete) for current_athlete in athletes]