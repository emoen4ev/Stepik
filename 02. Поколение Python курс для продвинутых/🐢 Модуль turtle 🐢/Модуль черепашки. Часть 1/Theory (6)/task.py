import turtle as t


def draw_regular_polygon(a, b):
    for _ in range(number_of_sides):
        t.forward(a)
        t.right(b)
    t.forward(a)


def draw_polygons(a, b):
    for _ in range(number_of_sides):
        draw_regular_polygon(a, b)
        t.left(b)


t.speed(10)

side_length = 100
number_of_sides = 6

angle = 360 / number_of_sides

draw_polygons(side_length, angle)

t.exitonclick()