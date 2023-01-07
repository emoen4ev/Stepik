import turtle as t


def draw_star(a, b):
    t.left(b)
    for _ in range(number_vertices):
        t.forward(a)
        t.left(180 - b)


side_length = 100
number_vertices = 5
angle = 180 / number_vertices

t.speed(8)

draw_star(side_length, angle)

t.exitonclick()