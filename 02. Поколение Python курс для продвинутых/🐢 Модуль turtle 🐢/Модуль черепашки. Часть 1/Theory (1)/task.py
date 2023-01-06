import turtle


def rectangle(width, height):
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)


x, y = 200, 100

rectangle(x, y)

turtle.exitonclick()