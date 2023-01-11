import turtle as t


def draw_circle():
    t.goto(x, y)
    t.pendown()
    t.circle(circle_radius)


t.speed(7)

circle_radius = 50
pen_width = 5
y_step = 10

colors = ('blue', 'yellow', 'black', 'green', 'red')
t.pensize(pen_width)
y_coord_first_row = -circle_radius
y_coord_second_row = -(2 * circle_radius + pen_width + y_step)
x_initial = -2 * (circle_radius + pen_width / 2)
x = x_initial
x_step = pen_width / 2

t.dot(10, 'purple')
t.hideturtle()

for i in range(len(colors)):
    t.penup()
    t.color(colors[i])
    y = y_coord_first_row if i % 2 == 0 else y_coord_second_row
    draw_circle()
    x += (circle_radius + x_step)

t.exitonclick()