from collections import deque

def bfs(graph, start = 0):
    if len(graph) <= 1:
        return '0', '1', '1'

    queue = deque([(start, 0)])

    results = []
    max_depht = 0
    while queue:
        node, level = queue.popleft()

        for neighbor in graph[node]:
            queue.append((neighbor, level + 1))
            if max_depht < level + 1:
                max_depht = level + 1
                results = [neighbor + 1]
            elif max_depht == level + 1:
                results.append(neighbor + 1)

    results.sort()
    return str(max_depht), str(len(results)), ' '.join(map(str, results))

def main():
    with open("input.txt", 'r') as file:
        data = list(map(int, file.read().split()))

    v_count = data[0]
    graph = [[] for _ in range(v_count)]


    for children, parent in enumerate(data[1:]):
        graph[parent - 1].append(children + 1)


    with open("output.txt", 'w') as file:
        file.write('\n'.join(bfs(graph)))

if __name__ == "__main__":
    main()

