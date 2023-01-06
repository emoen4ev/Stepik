import turtle as t


def many_squares(size, start, end, d):
    for angle in range(start, end + 1, d):
        draw_square(size, angle)


def draw_square(size, angle):
    t.setheading(angle)
    for _ in range(4):
        t.forward(size)
        t.left(90)


a = 100
start_angle = 20
end_angle = 60
diff = 20

many_squares(a, start_angle, end_angle, diff)

t.exitonclick()