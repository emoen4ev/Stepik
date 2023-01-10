import turtle as t
from math import sin, radians, cos
from random import randint


def draw_triangle(a, b):
    for _ in range(3):
        t.forward(a)
        t.left(b)


def draw_star():
    for _ in range(number_triangles):
        t.color(get_color())
        t.pendown()
        t.showturtle()
        draw_triangle(triangle_side_length, angle)
        t.penup()
        t.hideturtle()
        t.right(transition_angle)
        t.forward(polygon_side_size)
        t.left(new_starting_angle)


def get_color():
    r_g_b = (randint(0, 255), randint(0, 255), randint(0, 255))
    return r_g_b


t.speed(0)

t.Screen().setup(700, 700)
t.Screen().colormode(255)
t.Screen().bgcolor('black')
t.shape('turtle')
t.pensize(3)

number_triangles = 25
triangle_side_length = 300

tr_angle = 60
angle = 180 - tr_angle
number_polygon_sides = number_triangles * 3
inner_polygon_angle = 360 / number_polygon_sides
transition_angle = (180 - inner_polygon_angle - tr_angle) / 2
r = triangle_side_length / (2 * sin(radians(90 - (tr_angle / 2))))
polygon_side_size = 2 * r * sin(radians(inner_polygon_angle / 2))
new_starting_angle = 180 - (((180 - inner_polygon_angle) / 2) + tr_angle / 2)

initial_x = -triangle_side_length / 2
initial_y = -r / 2

t.penup()
t.hideturtle()
t.goto(initial_x, initial_y)

draw_star()

t.shapesize(4)
t.setheading(90)
t.goto(0, 0)
t.color(get_color())
t.stamp()
t.dot(10, get_color())

t.exitonclick()