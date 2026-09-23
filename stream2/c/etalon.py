import heapq


def dijkstra(graph, start):
    count_v = len(graph)
    distances = [float('inf') for _ in range(count_v)]
    distances[start] = 0


    previous = [None for _ in range(count_v)]

    heap = [(0, start)]

    while heap:
        w, v = heapq.heappop(heap)
        if w > distances[v]:
            continue

        for weight, vertex in graph[v]:
            new_dist = distances[v] + weight
            if new_dist < distances[vertex]:
                distances[vertex] = new_dist
                previous[vertex] = v
                heapq.heappush(heap, (new_dist, vertex))
    return distances, previous


def get_path(previous, target):
    path = []
    while target is not None:
        path.append(target)
        target = previous[target]


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

    distances, previous = dijkstra(graph, start)
    with open("output.txt", 'w') as file:
        file.write(' '.join(map(str, test(distances))))


if __name__ == "__main__":
    main()
