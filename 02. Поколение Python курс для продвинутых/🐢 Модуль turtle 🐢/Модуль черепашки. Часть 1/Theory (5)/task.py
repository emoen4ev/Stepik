import turtle as t


def draw_regular_polygon(a, b):
    for _ in range(number_of_sides):
        t.forward(a)
        t.left(b)


side_length = 150
number_of_sides = 6

angle = 360 / number_of_sides

draw_regular_polygon(side_length, angle)

t.exitonclick()