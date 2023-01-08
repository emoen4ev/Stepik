import turtle as t


t.pensize(15)
t.penup()
t.backward(160)
t.pendown()

for _ in range(10):
    t.circle(7)
    t.penup()
    t.forward(35)
    t.pendown()

t.speed(10)

t.exitonclick()