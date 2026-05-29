def welsh_powell(graph):
    v_count = len(graph) # длина графа

    # список вершин по количеству соседей (sorted всегда выплевывает список)
    order = sorted(range(v_count), key=lambda v: len(graph[v]), reverse=True)

    coloring = [0] * v_count # покрашенные вершины по индексам (индекс = номер вершины)

    for vertex in order:
        # выплевывает множество цветов уже покрашенных соседей (использованные цвета)
        neighbor_colors = {
            coloring[neighbour] for neighbour in graph[vertex] if coloring[neighbour] != 0
        }

        # меняем цвет пока не найдем не использованный соседями
        color = 1
        while color in neighbor_colors:
            color += 1

        # красим
        coloring[vertex] = color

    return coloring


def main():
    with open("input.txt", 'rb') as file:
        v_count, e_count = map(int, file.readline().split())

        graph = [[] for _ in range(v_count)]
        for _ in range(e_count):
            a, b = map(int, file.readline().split())
            a -= 1
            b -= 1
            graph[a].append(b)
            graph[b].append(a)


    result = welsh_powell(graph)

    with open("output.txt", 'w') as file:
        file.write('\n'.join([str(max(result)), ' '.join(map(str, result))]))


if __name__ == "__main__":
    main()
