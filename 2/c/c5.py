import heapq


def dijkstra(graph, start):
    count_v = len(graph)
    distances = [float('inf')] * count_v
    distances[start] = 0

    heap = [(0, start)]

    while heap:
        w, v = heapq.heappop(heap)
        if w > distances[v]:
            continue

        old_dist = distances[v]

        for weight, vertex in graph[v]:
            new_dist = old_dist + weight
            if new_dist < distances[vertex]:
                distances[vertex] = new_dist
                heapq.heappush(heap, (new_dist, vertex))

    return distances


def test(distance):
    return [-1 if i == float('inf') else i for i in distance]


def main():
    with open("input.txt", 'rb') as file:
        count_v, count_e, start = map(int, file.readline().split())
        start -= 1

        graph = [[] for _ in range(count_v)]
        for _ in range(count_e):
            vertex, neighbour, weight = map(int, file.readline().split())
            vertex -= 1
            neighbour -= 1
            graph[vertex].append((weight, neighbour))

    distances = dijkstra(graph, start)
    with open("output.txt", 'w') as file:
        file.write(' '.join(['-1' if i == float('inf') else str(i) for i in distances]))


if __name__ == "__main__":
    main()
