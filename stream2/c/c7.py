from collections import deque

def topo_kahn(graph):
    v_count = len(graph)
    in_degree = [0] * v_count

    # считаем зависимости
    for neighbours in graph:
        for vertex in neighbours:
            in_degree[vertex] += 1

    # если нет зависимостей можем выполнить сразу
    queue = deque([v for v in range(v_count) if in_degree[v] == 0])
    result = []

    while queue:
        vertex = queue.popleft()
        result.append(vertex) # выполнили сразу и записали

        for neighbour in graph[vertex]:
            in_degree[neighbour] -= 1
            # поскольку мы выполнили vertex проходим по всем соседям и вычитаем 1,
            # так как к ним требований стало на одну ед меньше

            if in_degree[neighbour] == 0:
                queue.append(neighbour)
                # если требований 0 выполняем

    if len(result) < len(graph):
        return [-2]
        # сли результат получился меньше верт

    return result


def main():
    with open("input.txt", 'rb') as file:
        v_count, e_count = map(int, file.readline().split())

        graph = [[] for _ in range(v_count)]
        for _ in range(e_count):
            vertex, neighbour = map(int, file.readline().split())
            vertex -= 1
            neighbour -= 1
            graph[vertex].append(neighbour)

    result = topo_kahn(graph)

    with open("output.txt", 'w') as file:
        file.write(' '.join(str(v + 1)  for v in result))


if __name__ == "__main__":
    main()