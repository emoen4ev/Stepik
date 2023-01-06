import turtle as t


def draw_rhombus(a, b):
    for i in range(4):
        t.forward(a)
        current_angle = 180 - b if i % 2 == 1 else b
        t.right(current_angle)


def draw_flower_of_rhombuses():
    for _ in range(number_rhombuses):
        draw_rhombus(side_length, angle)
        t.left(rotation_angle)


side_length = 100
angle = 60

number_rhombuses = 10

rotation_angle = 360 / number_rhombuses

t.speed(8)

draw_flower_of_rhombuses()

t.exitonclick()