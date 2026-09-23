import heapq

def prims(graph, start = 0):
    in_mst = set()
    mst_weight = 0

    heap_min = [(0, start, None)]

    while heap_min:
        weight, vertex, parent = heapq.heappop(heap_min)
        if vertex in in_mst:
            continue

        in_mst.add(vertex)
        if parent is not None:
            mst_weight += weight

        for neighbour, w in graph[vertex]:
            if neighbour not in in_mst:
                heapq.heappush(heap_min, (w, neighbour, vertex))

    return mst_weight


def main():
    with open("input.txt", 'rb') as file:
        v_count, e_count = map(int, file.readline().split())

        graph = [[] for _ in range(v_count)]
        for _ in range(e_count):
            a, b, weight = map(int, file.readline().split())
            a -= 1
            b -= 1
            graph[a].append((b, weight))
            graph[b].append((a, weight))

    result = prims(graph)

    with open("output.txt", 'w') as file:
        file.write((str(result)))


if __name__ == "__main__":
    main()