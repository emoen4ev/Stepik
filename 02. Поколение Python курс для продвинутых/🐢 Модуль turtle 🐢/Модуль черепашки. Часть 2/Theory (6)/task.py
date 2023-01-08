import turtle as t


t.speed(8)
t.Screen().setup(500, 500)
t.Screen().bgcolor('LightGreen')
t.shape('turtle')
t.penup()

k = 1.7
angle = 18

for i in range(50):
    t.stamp()
    t.forward(i * k)
    t.right(angle)

t.exitonclick()