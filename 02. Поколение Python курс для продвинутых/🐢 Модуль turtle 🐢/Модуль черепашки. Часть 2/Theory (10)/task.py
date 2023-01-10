import turtle as t


def draw_element(x_coord, y_coord):
    t.goto(x_coord, y_coord)
    t.dot(10, 'blue')




number_points = 10
step = 30
coord_y = -150
dots_line_length = (number_points - 1) * step
start_line = -int(dots_line_length / 2)
end_line = int(dots_line_length / 2)
x_y_coordinates = {i: coord_y for i in range(start_line, end_line, step)}
t.dot(15, 'red')
t.pencolor('green')

for x, y in x_y_coordinates.items():
    draw_element(x, y)


t.exitonclick()

# import turtle as T
# coord = {i: -100 for i in range(-100, 120, 20)}
# print(coord)
# T.dot(10, 'red')
# T.pencolor('green')
# for i in coord.items():
#   T.goto(i)
#   T.dot(10, 'blue')
#   T.penup()
#   T.goto(0,0)
#   T.pendown()
#
# T.exitonclick()