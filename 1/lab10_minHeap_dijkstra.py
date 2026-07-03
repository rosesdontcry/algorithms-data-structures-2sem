"""
Задание 1 — Взвешенный граф и алгоритм Дейкстры
================================================

Модуль реализует:
    * представление ориентированного взвешенного графа в виде списка
      смежности;
    * поиск кратчайших путей алгоритмом Дейкстры с использованием
      СОБСТВЕННОЙ реализации бинарной min-кучи (heapq в решении не
      используется как «чёрный ящик» — приоритетная очередь написана
      вручную, см. класс MinHeap);
    * восстановление кратчайшего пути по словарю предшественников;
    * анализ временной сложности реализованных алгоритмов
      (см. таблицу в конце файла).
"""
from itertools import count
from typing import Dict, List, Tuple, Optional
from collections import deque


Graph = Dict[int, List[Tuple[int, int]]]


class MinHeap:
    """Простая бинарная min-куча на массиве (списке Python).

    Хранит пары ``(приоритет, значение)``. Куча -- это полное бинарное
    дерево, представленное массивом, где для индекса ``i``:
        * левый потомок  -- ``2*i + 1``
        * правый потомок -- ``2*i + 2``
        * родитель       -- ``(i - 1) // 2``

    Операции:
        * ``push(item)``  -- добавить элемент в конец массива и
          «просеять» его вверх (``_sift_up``), пока не выполнится
          свойство кучи -> **O(log n)**;
        * ``pop()``       -- вернуть корень (минимум), поставить на его
          место последний элемент массива и «просеять» его вниз
          (``_sift_down``) -> **O(log n)**;
        * ``is_empty()``  -- проверка пустоты -> **O(1)**.
    """

    def __init__(self) -> None:
        self._data: List[Tuple[float, int]] = []

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def push(self, item: Tuple[float, int]) -> None:
        self._data.append(item)
        self._sift_up(len(self._data) - 1)

    def pop(self) -> Tuple[float, int]:
        if not self._data:
            raise IndexError("pop from empty heap")

        top = self._data[0]
        last = self._data.pop()
        if self._data:
            self._data[0] = last
            self._sift_down(0)
        return top

    def _sift_up(self, idx: int) -> None:
        while idx > 0:
            parent = (idx - 1) // 2
            if self._data[idx] < self._data[parent]:
                self._data[idx], self._data[parent] = self._data[parent], self._data[idx]
                idx = parent
            else:
                break

    def _sift_down(self, idx: int) -> None:
        n = len(self._data)
        while True:
            left = 2 * idx + 1
            right = 2 * idx + 2
            smallest = idx

            if left < n and self._data[left] < self._data[smallest]:
                smallest = left
            if right < n and self._data[right] < self._data[smallest]:
                smallest = right
            if smallest == idx:
                break

            self._data[idx], self._data[smallest] = self._data[smallest],self._data[idx]
            idx = smallest


def build_graph(file_name: str) -> Graph:
    with open(file_name, 'r') as file:
        count_v, count_e = map(int, file.readline().split())

        graph = {i: [] for i in range(count_v)}
        for _ in range(count_e):
            vertex, neighbour, weight = map(int, file.readline().split())
            graph[vertex].append((neighbour, weight))

    return graph


def print_graph(graph: Dict[int, List[Tuple[int, int]]]) -> None:
    for vertex in sorted(graph):
        print(f"{vertex}: {graph[vertex]}")


def dijkstra(graph: Graph, start: int) -> Tuple[Dict, Dict]:
    """Алгоритм Дейкстры на собственной приоритетной очереди (MinHeap).
    :param graph: список смежности
    :param start: стартовая вершина
    :return: пара словарей (dist, pred)
        * ``dist[v]`` -- кратчайшее расстояние от ``start`` до ``v``
        * ``pred[v]`` -- предшественник ``v`` на кратчайшем пути
    """
    dist: Dict[int, float] = {v: float("inf") for v in graph}
    pred: Dict[int, Optional[int]] = {v: None for v in graph}
    dist[start] = 0

    heap = MinHeap()
    heap.push((0, start))

    while not heap.is_empty():
        d, v = heap.pop()
        if d > dist[v]:
            continue

        for neighbour, weight in graph[v]:
            new_dist = d + weight
            if new_dist < dist[neighbour]:
                dist[neighbour] = new_dist
                pred[neighbour] = v
                heap.push((new_dist, neighbour))

    return dist, pred


def restore_path(pred: Dict, start: int, end: int) -> Optional:
    """
    :param pred: словарь предшественников, полученный из ``dijkstra``
    :param start: начальная вершина
    :param end: конечная вершина
    :return: список вершин пути ``[start, ..., end]`` или ``None``, если пути не существует.
    """
    if end not in pred:
        return None

    path = []
    current = end

    while current is not None:
        path.append(current)
        if current == start:
            break
        current = pred[current]
    else:
        return None

    path.reverse()

    if path[0] != start:
        return None

    return path


"""
Задание 2 — Критический путь на DAG
====================================

Модуль реализует:
    * топологическую сортировку DAG алгоритмом Кана
      (BFS с подсчётом входящих степеней);
    * поиск критического пути (самого длинного пути в DAG) методом
      динамического программирования по вершинам, взятым в
      топологическом порядке;
    * восстановление одного из критических путей и списка всех вершин,
      лежащих хотя бы на одном критическом пути;
    * анализ временной сложности (см. таблицу в конце файла).
"""

def topological_sort(graph: Dict[int, List[Tuple[int, int]]]) -> List[int]:
    """Топологическая сортировка алгоритмом Кана (BFS).
    Идея: вершина может быть выполнена, как только выполнены все её
    предшественники, т.е. когда её входящая степень становится равной 0.

    :param graph: список смежности
    :return: список вершин в топологическом порядке;
    """
    in_degree = {v: 0 for v in graph}

    for vertex in graph:
        for neighbour, _ in graph[vertex]:
            in_degree[neighbour] += 1

    queue = deque(v for v in graph if in_degree[v] == 0)
    order = []

    while queue:
        vertex = queue.popleft()
        order.append(vertex)

        for neighbour, _ in graph[vertex]:
            in_degree[neighbour] -= 1
            if in_degree[neighbour] == 0:
                queue.append(neighbour)

    if len(order) < len(graph):
        return [-2]

    return order


def _earliest_finish_times(graph: Graph, order: List[int]) -> Tuple[Dict, Dict]:
    """
    dist[v] = max(dist[u] + w) по всем рёбрам (u -> v, w), вычисляется при обходе вершин в топологическом порядке.
    :return: (dist, pred) - расстояния и предшественники на самом длинном пути от источника.
    """
    dist = {v: 0 for v in graph}
    pred = {}

    for u in order:
        for v, w in graph[u]:
            candidate = dist[u] + w
            if candidate > dist[v]:
                dist[v] = candidate
                pred[v] = u
    return dist, pred


def _remaining_longest_path(graph: Graph, order: List[int]) -> Dict:
    """Обратный проход DP: длина самого длинного пути от вершины до стока.
    ``rem[v] = max(w + rem[neighbour])`` по всем исходящим рёбрам,
    вычисляется при обходе вершин в ОБРАТНОМ топологическом порядке.
    """
    rem: Dict[int, int] = {v: 0 for v in graph}

    for u in reversed(order):
        for v, w in graph[u]:
            candidate = w + rem[v]
            if candidate > rem[u]:
                rem[u] = candidate

    return rem


def critical_path(graph: Graph) -> Tuple[int, List[int], List[int]]:
    """Находит критический путь (самый длинный путь) в DAG.
    Вершина ``v`` считается критической, если она лежит хотя бы на
    одном пути суммарной длины ``critical_time``, что эквивалентно
    условию ``dist[v] + rem[v] == critical_time``, где:
        * ``dist[v]`` -- самое раннее время завершения v (путь от истока);
        * ``rem[v]``  -- длина самого длинного пути от v до стока.

    :param graph: список смежности с весами
    :return: (critical_time, critical_nodes, path)
        * critical_time  - длина критического пути;
        * critical_nodes - отсортированный список всех вершин, лежащих хотя бы на одном критическом пути;
        * path - один из критических путей (список вершин).
    """
    order = topological_sort(graph)
    if order == [-2]:
        raise ValueError("Graph contains a cycle")

    dist, pred = _earliest_finish_times(graph, order)
    rem = _remaining_longest_path(graph, order)

    critical_time = max(dist.values())

    critical_nodes = sorted(
        v for v in graph if dist[v] + rem[v] == critical_time
    )

    end = max(dist, key=lambda v: dist[v])
    path = [end]

    while path[-1] in pred:
        path.append(pred[path[-1]])
    path.reverse()

    return critical_time, critical_nodes, path


def ex1():
    graph = build_graph("1.txt")

    #1.1
    print_graph(graph)
    print()

    #1.2
    start = 0
    dist, pred = dijkstra(graph, start)
    print(f"Distances from {start}: {dist}")

    #1.3
    start, end = 0, 4
    path = restore_path(pred, start, end)
    if path is None:
        print(f"No path from {start} to {end}")
    else:
        print(f"Shortest path {start} -> {end}: {path}, length: {dist[end]}")


def ex2():
    graph = build_graph("2.txt")

    #2.1
    order = topological_sort(graph)
    print(f"Topological order: {order}")

    #2.2
    critical_time, critical_nodes, path = critical_path(graph)
    print(f"Critical time: {critical_time}")
    print(f"Critical nodes: {critical_nodes}")
    print(f"Critical path: {path}")
    print()

    #2.3
    dist, _ = _earliest_finish_times(graph, order)
    print("Earliest finish times:")
    for v in sorted(dist):
        print(f"  Node {v}: {dist[v]}")

if __name__ == "__main__":
    ex2()
