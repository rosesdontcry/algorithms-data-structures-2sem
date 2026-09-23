from collections import deque


def bfs(graph, e_count, start = 0):
    v_count = len(graph)
    if v_count - 1 != e_count:
        return "NO"

    used_bfs = [False] * v_count

    used_bfs[start] = True
    queue = deque([(start, start)])

    while queue:
        node, parent = queue.popleft()

        for neighbor in graph[node]:
            if not used_bfs[neighbor]:
                used_bfs[neighbor] = True
                queue.append((neighbor, node))

            else:
                if parent != neighbor:
                    return "NO"
    return "YES" if all(used_bfs) else "NO"

def main():
    with open("input.txt", 'r') as file:
        v_count, e_count = map(int, file.readline().split())
        graph = [[] for _ in range(v_count)]

        for _ in range(e_count):
            a, b = map(int, file.readline().split())
            a, b = a - 1, b - 1
            graph[a].append(b)
            graph[b].append(a)


    with open("output.txt", 'w') as file:
        file.write(str(bfs(graph, e_count)))

if __name__ == "__main__":
    main()

