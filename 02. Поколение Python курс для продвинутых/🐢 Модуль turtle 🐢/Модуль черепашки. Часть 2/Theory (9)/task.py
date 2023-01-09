import turtle as t
from math import sin, pi

t.speed(1)


def draw_triangle(a, b):
    for _ in range(3):
        t.forward(a)
        t.left(b)


def draw_star():
    for _ in range(number_triangles):
        draw_triangle(triangle_side_length, angle)
        t.right(transition_angle)
        print(transition_angle)
        t.penup()
        t.forward(polygon_side_size)
        t.left(transition_angle - 90)
        t.pendown()


triangle_side_length = 150
tr_angle = 60
angle = 180 - tr_angle
number_triangles = 2
number_polygon_sides = number_triangles * 3
transition_angle = 360 / number_polygon_sides
polygon_side_size = 2 * triangle_side_length * ((3 ** 1 / 3) / 3) * sin(pi / number_polygon_sides)

# draw_triangle(triangle_side_length, angle)
draw_star()

t.exitonclick()