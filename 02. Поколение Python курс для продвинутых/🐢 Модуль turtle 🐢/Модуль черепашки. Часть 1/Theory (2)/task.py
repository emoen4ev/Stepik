import turtle


def triangle(side):
    turtle.forward(side)
    turtle.setheading(120)
    turtle.forward(side)
    turtle.setheading(240)
    turtle.forward(side)


a = 100

triangle(a)

turtle.exitonclick()