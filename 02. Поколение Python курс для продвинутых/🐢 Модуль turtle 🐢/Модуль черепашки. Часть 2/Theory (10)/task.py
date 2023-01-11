import turtle as t


def draw_forward(coord_x):
    t.goto(coord_x, coord_y)
    t.dot(6, 'blue')


def draw_backward(coord_x):
    t.penup()
    t.goto(coord_x, coord_y)
    t.dot(6, 'blue')
    t.pendown()
    t.goto(0, 0)


t.speed(4)
t.hideturtle()
t.pencolor('green')
t.dot(6, 'red')

coord_y = -150
number_points = 17
step = 39

dots_line_length = (number_points - 1) * step
start_line = -int(dots_line_length / 2)
end_line = int(dots_line_length / 2) + step
x_coordinates = tuple(coord_x for coord_x in range(start_line, end_line, step))

for i in range(len(x_coordinates)):
    draw_forward(x_coordinates[i]) if i % 2 == 0 else draw_backward(x_coordinates[i])

t.exitonclick()