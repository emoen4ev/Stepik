import turtle as t
from random import randint


t.speed(10)
t.Screen().colormode(255)

radius = 7
pen_with = 2 * radius

number_circles = 10
step = 55
start_point = ((number_circles - 1) / 2) * step

t.pensize(pen_with)
t.penup()
t.backward(start_point)
t.pendown()

for _ in range(number_circles):
    r_g_b = tuple(randint(0, 255) for _ in range(3))
    t.pencolor(*r_g_b)
    t.circle(radius)
    t.penup()
    t.forward(step)
    t.pendown()

t.exitonclick()