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


def point_in_polygon(px: float, py: float, polygon: list[Point]) -> bool:
    count = 0



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



if __name__ == "__main__":
    ex1()
