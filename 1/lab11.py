from math import sqrt

Point = tuple[float, float]


def dist(a: Point, b: Point) -> float:
    """
    Вычисляет евклидово расстояние между двумя точками
    d(A, B) = √((x₂ - x₁)² + (y₂ - y₁)²)
    """
    return sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)


def perimeter(polygon: list[Point]) -> float:
    """
    Вычисляет периметр многоугольника путем складывания результатов функции dist
    polygon[1:] + [polygon[0]] - делает сдвиг списка
    """
    return sum(map(dist, polygon, polygon[1:] + [polygon[0]]))


def area(polygon: list[Point]) -> float:
    """
    Вычисляет площадь многоугольника по формуле Гаусса
    S = ½ · | ∑ (xᵢ₋₁·yᵢ - xᵢ·yᵢ₋₁) |
    Использует отрицательную индексацию для автоматического замыкания последней вершины с первой
    """
    return 0.5 * abs(sum(
        (polygon[i - 1][0] * polygon[i][1]) - (polygon[i][0] * polygon[i - 1][1]) for i in range(len(polygon))
    ))


########################################################################################################################


def _point_in_polygon(px: float, py: float, polygon: list[Point]) -> bool:
    count = sum(1 for i in range(len(polygon)) if
                 min(polygon[i - 1][1], polygon[i][1]) < py <= max(polygon[i - 1][1], polygon[i][1]) and
                 px < ((py - polygon[i - 1][1]) * (polygon[i][0] - polygon[i - 1][0]) /
                       (polygon[i][1] - polygon[i - 1][1]) + polygon[i - 1][0]))

    return count % 2 != 0


def point_in_polygon_(px: float, py: float, polygon: list[Point]) -> bool:
    inside = False

    for i in range(len(polygon)):
        p1x, p1y = polygon[i - 1]
        p2x, p2y = polygon[i]

        if min(p1y, p2y) < py <= max(p1y, p2y):
            x_intersect = (py - p1y) * (p2x - p1x) / (p2y - p1y) + p1x

            if px < x_intersect:
                inside = not inside

    return inside



def point_in_polygon(px: float, py: float, polygon: list[Point]) -> None:
    if  _point_in_polygon(px, py, polygon):
        print(f"({px}, {py}): INSIDE")
    else:
        print(f"({px}, {py}): OUTSIDE")


##########################################################################################################


def cross(o: Point, a: Point, b: Point) -> float:
    return ((a[0] - o[0]) * (b[1] - o[1])) - ((a[1] - o[1]) * (b[0] - o[0]))


def on_segment(p: Point, r: Point, q: Point) -> bool:
    return (min(p[0], r[0]) <= q[0] <= max(p[0], r[0])) and \
            min(p[1], r[1]) <= q[1] <= max(p[1], r[1])


def _segments_intersect(a: Point, b: Point , c: Point ,d: Point) -> bool:
    d1 = cross(a, b, c)
    d2 = cross(a, b, d)
    d3 = cross(c, d, a)
    d4 = cross(c, d, b)

    if ((d1 > 0 > d2) or (d1 < 0 < d2)) and \
        ((d3 > 0 > d4) or (d3 < 0 < d4)):
        return True

    if d1 == 0 and on_segment(a, b, c): return True
    if d2 == 0 and on_segment(a, b, d): return True
    if d3 == 0 and on_segment(c, d, a): return True
    if d4 == 0 and on_segment(c, d, b): return True
    return False


def segments_intersect(a: Point, b: Point, c: Point, d: Point) -> None:
    print(f"AB = ({a[0]}, {a[1]}) - ({b[0]}, {b[1]}), "
          f"CD = ({c[0]}, {c[1]}) - ({d[0]}, {d[1]}) "
          f"-> {_segments_intersect(a, b, c, d)}")


def polygon_inserts(poly1: list[Point], poly2: list[Point]) -> bool:
    edges1 = zip(poly1, poly1[1:] + [poly1[0]])
    edges2 = zip(poly2, poly2[1:] + [poly2[0]])

    for a, b in edges1:
        for c, d in edges2:
            if _segments_intersect(a, b, c, d):
                return True

    px, py = poly1[0]
    if _point_in_polygon(px, py, poly2):
        return True

    px, py = poly2[0]
    if _point_in_polygon(px, py, poly1):
        return True

    return False


################################################################################################################33


def ex1():
    rectangle = [(0, 0), (5, 0), (5, 3), (0, 3)]
    print(f"Rectangle {rectangle}:\n"
          f"\tPerimetr: {perimeter(rectangle)}\n"
          f"\tArea: {area(rectangle)}\n")

    triangle = [(0, 0), (6, 0), (3, 4)]
    print(f"Triangle {triangle}:\n"
          f"\tPerimetr: {perimeter(triangle)}\n"
          f"\tArea: {area(triangle)}\n")


def ex2():
    polygon = [(0, 0), (4, 0), (4, 2), (2, 2), (2, 4), (0, 4)]

    point_in_polygon(1, 1, polygon)
    point_in_polygon(3, 3, polygon)
    point_in_polygon(5, 1, polygon)
    point_in_polygon(1, 3, polygon)


def ex3():
    segments_intersect((0, 0), (4, 4), (0, 4), (4, 0))
    segments_intersect((0, 0), (2, 0), (3, 0), (5, 0))
    segments_intersect((0, 0), (3, 0), (1, 0), (4, 0))
    segments_intersect((0, 0), (2, 2), (2, 2), (4, 0))
    segments_intersect((0, 0), (1, 1), (2, 0), (3, 1))


    # Сценарий 1: пересекающиеся (перекрывающиеся рамки)
    poly1 = [(0, 0), (4, 0), (4, 4), (0, 4)]
    poly2 = [(2, 2), (6, 2), (6, 6), (2, 6)]

    print(polygon_inserts(poly1, poly2))

    # Сценарий 2: раздельные многоугольники
    poly1 = [(0, 0), (2, 0), (2, 2), (0, 2)]
    poly2 = [(3, 3), (5, 3), (5, 5), (3, 5)]

    print(polygon_inserts(poly1, poly2))

    # Сценарий 3: один внутри другого (без пересечения рёбер)
    poly1 = [(0, 0), (6, 0), (6, 6), (0, 6)]
    poly2 = [(1, 1), (2, 1), (2, 2), (1, 2)]

    print(polygon_inserts(poly1, poly2))


if __name__ == "__main__":
    ex1()
    ex2()
    ex3()
