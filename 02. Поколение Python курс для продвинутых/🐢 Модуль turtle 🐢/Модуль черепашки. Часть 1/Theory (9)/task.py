import turtle as t


def draw_line(a):
    t.forward(a)
    t.backward(a)


def draw_figure(a, b):
    for _ in range(number_lines):
        draw_line(a)
        t.left(b)


side_length = 100
number_lines = 12
angle = 360 / number_lines

t.speed(8)

draw_figure(side_length, angle)

t.exitonclick()