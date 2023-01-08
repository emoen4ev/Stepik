import turtle as t

t.Screen().setup(500, 500)
t.Screen().bgcolor('LightSkyBlue')

t.speed(4)
t.shape('turtle')
t.shapesize(1.5, 1)
t.pensize(4)
t.penup()

part_1 = 150
part_2 = 20
part_3 = 20
back_path = part_1 + part_2 + part_3
angle = 360 / 12


def draw_ray():
    t.forward(part_1)
    t.pendown()
    t.color('navy')
    t.forward(part_2)
    t.penup()
    t.forward(part_3)
    t.color('red')
    t.stamp()
    t.backward(back_path)


for _ in range(12):
    draw_ray()
    t.left(angle)

t.exitonclick()