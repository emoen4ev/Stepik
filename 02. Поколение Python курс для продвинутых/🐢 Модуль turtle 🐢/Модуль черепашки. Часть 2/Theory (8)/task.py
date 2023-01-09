import turtle

turtle.speed(0)

for i in range(-100, 101):
    turtle.circle(100 - 10 * i)

turtle.exitonclick()