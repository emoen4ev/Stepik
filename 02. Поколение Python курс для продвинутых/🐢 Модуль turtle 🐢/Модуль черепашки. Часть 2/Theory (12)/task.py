import turtle as t
from math import sin, cos, radians


t.speed(6)
t.hideturtle()

size = 300

# t.dot(5, 'purple')
t.penup()
t.goto(0, -size)
t.pendown()

t.circle(size)
t.circle(size * 0.55)
t.penup()
t.goto(0, -(size - 0.25 * size))
t.pendown()
t.goto(0, -(size - 0.7 * size))
t.circle(size * 0.1)
t.penup()
t.goto(0, (-size + size * 0.55))
# t.dot(5, 'purple')
t.penup()
t.goto(cos(radians(10)) * ((size * 0.55) / 2 + size * 0.2), sin(radians(10)) * ((size * 0.55) / 2 + size * 0.2))
t.dot(int(size * 0.2), 'black')
t.goto(-cos(radians(10)) * ((size * 0.55) / 2 + size * 0.2), sin(radians(10)) * ((size * 0.55) / 2 + size * 0.2))
t.dot(int(size * 0.2), 'black')
t.goto(-cos(radians(45)) * (size + size * 0.06), sin(radians(45)) * (size + size * 0.06))
t.pendown()
t.circle(size * 0.25)
t.penup()
t.goto(cos(radians(45)) * (size + size * 0.06), sin(radians(45)) * (size + size * 0.06))
t.pendown()
t.circle(size * 0.25)

t.exitonclick()