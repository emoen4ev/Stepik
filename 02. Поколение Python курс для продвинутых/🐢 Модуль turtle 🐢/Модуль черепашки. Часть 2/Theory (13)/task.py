import turtle as t
from random import randint


def draw_ray(x, y, s):
    t.penup()
    t.goto(x, y)
    s = s / (snowflake_ray_parts + 1)
    t.pendown()
    for _ in range(snowflake_ray_parts):
        t.forward(s)
        for i in range(2):
            angle = 45 if i % 2 == 0 else -90
            t.left(angle)
            t.forward(s)
            t.backward(s)
        t.left(45)
    t.forward(s)
    t.goto(x, y)


def draw_snowflake():
    t.pencolor(*get_snowflake_color())
    s = get_snowflake_size()
    x, y = get_snowflake_coordinates(s + 5)
    for _ in range(snowflake_number_rays):
        draw_ray(x, y, s)
        t.left(rays_angle)


def get_snowflake_color():
    r_g_b = tuple(randint(0, 255) for _ in range(3))
    return r_g_b


def get_snowflake_size():
    snowflake_size = randint(snowflakes_min_size, snowflakes_max_size)
    return snowflake_size


def get_snowflake_coordinates(a):
    x_coord, y_coord = randint(-screen_width / 2 + a, screen_width / 2 - a), \
        randint(-screen_height / 2 + a, screen_height / 2 - a)
    return x_coord, y_coord


t.speed(0)
screen_width = 1000
screen_height = 1000
t.Screen().setup(screen_width, screen_height)
t.Screen().colormode(255)
t.Screen().bgcolor('AliceBlue')
t.pensize(2)
t.hideturtle()

min_number_snowflakes = 5
max_number_snowflakes = 15
snowflakes_min_size = 15
snowflakes_max_size = 100
snowflake_ray_parts = 3
snowflake_number_rays = 8

number_snowflakes = randint(min_number_snowflakes, max_number_snowflakes)
print(number_snowflakes)

rays_angle = 360 / snowflake_number_rays

for _ in range(number_snowflakes):
    draw_snowflake()

t.exitonclick()