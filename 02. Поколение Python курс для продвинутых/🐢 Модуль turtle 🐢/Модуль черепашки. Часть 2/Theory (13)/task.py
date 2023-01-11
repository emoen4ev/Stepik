import turtle as t
from random import randint

screen_width = 1000
screen_height = 1000
t.Screen().setup(screen_width, screen_height)
t.Screen().colormode(255)


def draw_ray(x, y, s):
    t.penup()
    t.goto(x, y)
    s = s / (ray_parts + 1)
    t.pendown()
    for _ in range(ray_parts):
        t.forward(s)
        for i in range(2):
            angle = 45 if i % 2 == 0 else -90
            t.left(angle)
            t.forward(s)
            t.backward(s)
        t.left(45)
    t.forward(s)
    t.goto(x, y)


def draw_snowflake(x, y):
    t.pencolor(*get_color())
    s = get_size()
    for _ in range(number_rays):
        draw_ray(x, y, s)
        t.left(rays_angle)


def get_color():
    r_g_b = tuple(randint(0, 255) for _ in range(3))
    return r_g_b


def get_size():
    snowflake_size = randint(snowflakes_min_size, snowflakes_max_size)
    return snowflake_size


t.speed(0)

snowflakes_min_size = 15
snowflakes_max_size = 100
ray_parts = 3
number_rays = 8

rays_angle = 360 / number_rays

draw_snowflake(0, 0)

t.exitonclick()