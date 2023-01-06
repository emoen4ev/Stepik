import turtle as t


def draw_4_squares(a,angle):
    for _ in range(4):
        t.setheading(angle)
        for _ in range(4):
            t.forward(a)
            t.left(90)
        angle += 90


def draw_many_squares(a, start, end, d):
    for angle in range(start, end + 1, d):
        draw_4_squares(a, angle)


side = 150
start_angle = 0
end_angle = 45
diff = 45

draw_many_squares(side, start_angle, end_angle, diff)

t.exitonclick()