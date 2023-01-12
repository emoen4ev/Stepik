import turtle as t
from random import randint, randrange


def draw_ray(x, y, s):
    t.penup()
    t.goto(x, y)
    s_part = s / (snowflake_ray_parts + 1)
    t.pendown()
    for _ in range(snowflake_ray_parts):
        t.forward(s_part)
        for i in range(2):
            angle = 45 if i % 2 == 0 else -90
            t.left(angle)
            t.forward(s_part)
            t.backward(s_part)
        t.left(45)
    t.forward(s_part)
    t.goto(x, y)


def draw_snowflake(i):
    t.pencolor(*get_snowflake_color())
    x, y, s = get_snowflakes_data(i)
    for _ in range(snowflake_number_rays):
        draw_ray(x, y, s)
        t.left(rays_angle)


def get_snowflake_color():
    r_g_b = tuple(randint(0, 255) for _ in range(3))
    return r_g_b


def get_snowflake_size():
    snowflake_size = randrange(snowflakes_min_size, snowflakes_max_size + 1, snowflakes_step_size)
    return snowflake_size


def get_snowflake_coordinates(min_dist):
    x_coord, y_coord = randint(-(screen_width / 2) + min_dist, (screen_width / 2) - min_dist), \
        randint(-(screen_height / 2) + min_dist, (screen_height / 2) - min_dist)
    return x_coord, y_coord


def get_snowflakes_data(i):
    s = get_snowflake_size()
    x, y = get_snowflake_coordinates(s + min_distance_from_screen_borders)
    if snowflakes_data:
        x, y, s = validate_snowflake_data(x, y, s)
    key = f'snowflake: {i}'
    snowflakes_data[key] = [x, y, s]
    return snowflakes_data[key]


def validate_snowflake_data(cur_x, cur_y, cur_s):
    while True:
        is_data_correct = True
        for v in snowflakes_data.values():
            if (abs(max(v[0], cur_x) - min(v[0], cur_x)) <= (v[2] + cur_s)) and (
                    abs(max(v[1], cur_y) - min(v[1], cur_y)) <= (v[2] + cur_s)):
                is_data_correct = False
                break
        if not is_data_correct:
            cur_s = get_snowflake_size()
            cur_x, cur_y = get_snowflake_coordinates(cur_s + min_distance_from_screen_borders)
            continue
        else:
            break
    return cur_x, cur_y, cur_s


t.speed(0)
screen_width = 1000
screen_height = 1000
t.Screen().setup(screen_width, screen_height)
t.Screen().colormode(255)
t.Screen().bgcolor('AliceBlue')
t.pensize(2)
t.hideturtle()

min_number_snowflakes = 10
max_number_snowflakes = 30
snowflakes_min_size = 15
snowflakes_max_size = 80
snowflakes_step_size = 5
snowflake_ray_parts = 3
snowflake_number_rays = 8
min_distance_from_screen_borders = 10

number_snowflakes = randint(min_number_snowflakes, max_number_snowflakes)
# print(f'number_snowflakes: {number_snowflakes}')

rays_angle = 360 / snowflake_number_rays

snowflakes_data = dict()

for i in range(1, number_snowflakes + 1):
    draw_snowflake(i)

t.exitonclick()