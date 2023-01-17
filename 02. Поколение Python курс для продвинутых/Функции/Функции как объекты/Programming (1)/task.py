def get_distance(current_point: tuple) -> float:
    current_x_coord = current_point[0]
    current_y_coord = current_point[1]

    # return (current_x_coord ** 2 + current_y_coord ** 2) ** 1 / 2  # Если точно следовать формуле ...
    return current_x_coord ** 2 + current_y_coord ** 2  # Этого вполне достаточно ...


points = [
    (-1, 1),
    (5, 6),
    (12, 0),
    (4, 3),
    (0, 1),
    (-3, 2),
    (0, 0),
    (-1, 3),
    (2, 0),
    (3, 0),
    (-9, 1),
    (3, 6),
    (8, 8),
]

print(sorted(points, key=get_distance))