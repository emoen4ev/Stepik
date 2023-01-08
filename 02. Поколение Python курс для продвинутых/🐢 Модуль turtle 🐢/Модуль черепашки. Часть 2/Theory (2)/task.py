import turtle as t
from random import randint


t.Screen().colormode(255)
t.speed(3)

side_a_length = 150
side_b_length = 75
pen_size = 3
t.pensize(pen_size)
dot_size = 20
angle = 90

for i in range(4):
    dot_color = randint(0, 255), randint(0, 255), randint(0, 255)
    t.dot(dot_size, dot_color)
    side_length = side_a_length if i % 2 == 0 else side_b_length
    t.forward(side_length)
    t.left(angle)

t.exitonclick()