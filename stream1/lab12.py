import math

def translate(points: list[tuple], tx: float, ty: float) -> list[tuple]:
    """Сдвиг набора точек на вектор (tx, ty)."""
    return [(x + tx, y + ty) for x, y in points]


def rotate(points: list[tuple], angle_deg: float) -> list[tuple]:
    """
    Поворот точек вокруг начала координат на angle_deg (против часовой стрелки).
    Используем матрицу R из справочника:
        x' = x*cosθ - y*sinθ
        y' = x*sinθ + y*cosθ
    """
    theta = math.radians(angle_deg)
    cos_t, sin_t = math.cos(theta), math.sin(theta)
    result = []
    for x, y in points:
        x_new = x * cos_t - y * sin_t
        y_new = x * sin_t + y * cos_t
        result.append((x_new, y_new))
    return result


def scale(points: list[tuple], sx: float, sy: float) -> list[tuple]:
    """Масштабирование точек относительно начала координат."""
    return [(x * sx, y * sy) for x, y in points]


def rotate_around_point(points, angle_deg, cx, cy):
    """Поворот вокруг произвольной точки (cx, cy): T(-c) -> R(θ) -> T(c)."""
    shifted = translate(points, -cx, -cy)
    rotated = rotate(shifted, angle_deg)
    return translate(rotated, cx, cy)


def round_points(points, ndigits=4):
    return [(round(x, ndigits), round(y, ndigits)) for x, y in points]

square = [(0, 0), (2, 0), (2, 2), (0, 2)]

print("Original: ", square)

scaled = scale(square, 1.5, 1.5)
print("\nAfter scale(1.5, 1.5):")
print(" ", round_points(scaled))

rotated = rotate(scaled, 45)
print("\nAfter rotate(45°):")
print(" ", round_points(rotated))

translated = translate(rotated, 5, 3)
print("\nAfter translate(5, 3):")
print(" ", round_points(translated))

def cross(o, a, b):
    """Векторное произведение (A-O) x (B-O)."""
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def jarvis_hull(points: list[tuple]) -> list[tuple]:
    """
    Построение выпуклой оболочки методом Джарвиса (Gift Wrapping).
    Возвращает вершины в порядке обхода против часовой стрелки (CCW).
    """
    pts = list(dict.fromkeys(points))  # убираем дубликаты, сохраняя порядок
    n = len(pts)
    if n < 3:
        return pts[:]

    # старт: самая левая точка, при равенстве x — самая нижняя
    start = min(pts, key=lambda p: (p[0], p[1]))

    hull = []
    current = start

    while True:
        hull.append(current)
        endpoint = pts[0] if pts[0] != current else pts[1]

        for candidate in pts:
            if candidate == current:
                continue
            c = cross(current, endpoint, candidate)

            if endpoint == current or c < 0:
                # candidate находится правее (по часовой стрелке) —
                # значит текущий endpoint не крайний, обновляем
                endpoint = candidate
            elif c == 0:
                # коллинеарные точки — оставляем только САМУЮ ДАЛЬНЮЮ,
                # чтобы промежуточные точки не попадали в оболочку
                d_cur = (endpoint[0]-current[0])**2 + (endpoint[1]-current[1])**2
                d_new = (candidate[0]-current[0])**2 + (candidate[1]-current[1])**2
                if d_new > d_cur:
                    endpoint = candidate

        current = endpoint
        if current == start:
            break

    return hull

points = [(0,0), (2,0), (4,0), (4,4), (2,4), (0,4), (0,2), (1,2), (2,1), (3,3)]

hull = jarvis_hull(points)

print(f"Input points ({len(points)}): {points}")
print(f"\nJarvis hull ({len(hull)} vertices): {hull}")

def graham_hull(points: list[tuple]) -> list[tuple]:
    """
    Построение выпуклой оболочки методом Грэхема.
    Возвращает вершины в порядке CCW.

    Стратегия при равном полярном угле:
        оставляем только САМУЮ ДАЛЬНЮЮ точку от опорной.
        Это делает результат идентичным алгоритму Джарвиса
        (без "лишних" коллинеарных точек на рёбрах оболочки).
    """
    pts = list(dict.fromkeys(points))
    if len(pts) < 3:
        return pts[:]

    # опорная точка: минимальный y, при равенстве — минимальный x
    start = min(pts, key=lambda p: (p[1], p[0]))
    others = [p for p in pts if p != start]

    def angle_dist(p):
        dx, dy = p[0] - start[0], p[1] - start[1]
        return (math.atan2(dy, dx), dx*dx + dy*dy)

    others.sort(key=angle_dist)

    # группируем по углу, оставляем самую дальнюю точку в группе
    filtered = []
    i = 0
    n = len(others)
    while i < n:
        j = i
        base_angle = angle_dist(others[i])[0]
        while j + 1 < n and abs(angle_dist(others[j+1])[0] - base_angle) < 1e-9:
            j += 1
        filtered.append(others[j])   # т.к. сортировка по dist по возрастанию
        i = j + 1

    if len(filtered) < 2:
        return [start] + filtered

    stack = [start, filtered[0]]
    for p in filtered[1:]:
        while len(stack) > 1 and cross(stack[-2], stack[-1], p) <= 0:
            stack.pop()
        stack.append(p)

    return stack

points = [(0,0), (2,0), (4,0), (4,4), (2,4), (0,4), (0,2), (1,2), (2,1), (3,3)]

jarvis_result = jarvis_hull(points)
graham_result = graham_hull(points)

print(f"Points: {points}\n")
print(f"Jarvis hull  ({len(jarvis_result)} vertices): {jarvis_result}")
print(f"Graham hull  ({len(graham_result)} vertices): {graham_result}")

match = set(jarvis_result) == set(graham_result)
print(f"\nVertex sets match: {match}")

