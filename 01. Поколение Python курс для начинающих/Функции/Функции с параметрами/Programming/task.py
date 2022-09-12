def draw_triangle(fill_parametric_variable, base_parametric_variable):
    counter = 0
    for row in range(base_parametric_variable):
        if row <= base_parametric_variable / 2:
            counter += 1
        else:
            counter -= 1
        print(fill_parametric_variable * counter)


fill = input()
base = int(input())

draw_triangle(fill, base)
