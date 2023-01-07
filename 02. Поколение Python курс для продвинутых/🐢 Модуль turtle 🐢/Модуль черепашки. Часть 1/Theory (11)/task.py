import turtle as t


def draw_square(a, b):
    t.setheading(180)
    for _ in range(4):
        t.forward(a)
        t.right(b)


def draw_figure(a, b):
    for _ in range(number_squares):
        draw_square(a, b)
        a += step


side_length = 100
angle = 90
number_squares = 10
step = 15

draw_figure(side_length, angle)

t.speed(6)

t.exitonclick()