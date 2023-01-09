import turtle as t


t.Screen().setup(1000, 1000)
t.speed(6)

colors = ['red', 'blue', 'yellow', 'green', 'purple', 'orange']
number_sides = 8
initial_side_size = 12
angle = 360 / number_sides
number_circles = 5

for i in range(number_circles * number_sides):
    t.left(angle)
    t.pensize(i)
    current_color = colors[i % len(colors)]
    t.color(current_color)
    side_size = initial_side_size + i / 3
    t.forward(side_size)
    initial_side_size = side_size

t.exitonclick()