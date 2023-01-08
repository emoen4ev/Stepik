import turtle as t
from random import randint

t.Screen().colormode(255)
t.speed(5)

number_rays = 8
angle = 360 / number_rays
ray_length = 150

t.shape('triangle')
t.shapesize(1, 2)

dot_color = 'red'
dot_size = 30

for _ in range(number_rays):
    t.pendown()
    t.forward(ray_length)
    r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
    t.color(r, g, b)
    t.stamp()
    t.color('black')
    t.penup()
    t.backward(ray_length)
    t.left(angle)

t.shape('classic')
t.color(dot_color)
t.dot(dot_size, dot_color)

t.exitonclick()