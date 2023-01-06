import turtle as t


def draw_rhombus(a, b):
    for i in range(4):
        t.forward(a)
        current_angle = 180 - b if i % 2 == 1 else b
        t.right(current_angle)


side_length = 100
angle = 60

draw_rhombus(side_length, angle)

t.exitonclick()