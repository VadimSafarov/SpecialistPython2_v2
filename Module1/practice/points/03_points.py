class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
def distance(p1, p2):
    """
    Расстояние между двумя точками
    """
    dist = ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5
    return dist

# Дан список точек
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]

# Задание: найдите точку наиболее удаленную от начала координат и выведите ее координаты

# TODO: your core here...
point_zero = Point(0, 0)
lengthmax = 0
for i in range(0, len(points)):
    length = distance(points[i], point_zero)
    if length > lengthmax:
        lengthmax = length

print("Координаты наиболее удаленной точки = ", lengthmax)
