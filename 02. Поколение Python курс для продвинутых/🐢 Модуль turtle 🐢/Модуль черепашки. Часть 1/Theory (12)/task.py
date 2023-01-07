import turtle as t


def draw_figure(a, b):
    t.setheading(90)
    for _ in range(number_sides):
        t.forward(a)
        t.left(b)
        a += step
    t.forward(a)


initial_size = 30
angle = 90
step = 10
number_sides = 20

draw_figure(initial_size, angle)

t.speed(15)

t.exitonclick()

# import turtle
# from numpy import arange
#
#
# def curve(angle, size, max_len):
#     turtle.tracer(0, 0)
#     turtle.pensize(size)
#
#     for i in arange(0, max_len, .9):
#         turtle.left(angle)
#         turtle.forward(i)
#     turtle.goto(0, 0)
#
#
# turtle.hideturtle()
# for angle in arange(222, 270, .05):
#     turtle.clear()
#     curve(angle, 1, 3000)
#     turtle.update()
# turtle.mainloop()