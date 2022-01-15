class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance(p1, p2):
    dist = ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5
    return dist


point1 = Point(0, 0)
point2 = Point(5, 0)

d = distance(point1,point2)

print("Расстояние между точками = ", d)
