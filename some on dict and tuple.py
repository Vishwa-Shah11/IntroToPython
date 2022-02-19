points = [ ]
for x in range(0, 5):
    for y in range(0, 5):
        points.append((x, y))

print(points)

def color_it(points):
    colored_points = dict()
    for point in points:
        x, y = point
        if x + y == 4:
            colored_points[point] = 'red'
        elif x + y > 4:
            colored_points[point] = 'yellow'
        elif x + y < 4:
            colored_points[point] = 'green'
    return colored_points

print(color_it(points))