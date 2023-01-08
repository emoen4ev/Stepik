import turtle as t


t.speed(5)
t.shape('turtle')
t.shapesize(2, 2)

t.penup()

ray_length = 250
number_turtle_rays = 10
angle = 360 / number_turtle_rays

for _ in range(number_turtle_rays):
    t.forward(ray_length)
    t.stamp()
    t.backward(ray_length)
    t.left(angle)

t.exitonclick()