def dfs(graph):
    v_count = len(graph)
    visited = [False] * v_count
    count_components = 0

    def _dfs(node):
        visited[node] = True

        for neighbor in graph[node]:
            if not visited[neighbor]:
                _dfs(neighbor)

    for i in range(v_count):
        if not visited[i]:
            _dfs(i)
            count_components +=1

    return count_components

def dfs_iterative(graph):
    v_count = len(graph)
    visited = [False] * v_count
    count_components = 0

    for i in range(v_count):
        if not visited[i]:
            count_components += 1
            stack = [i]
            visited[i] = True

            while stack:
                node = stack.pop()
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)

    return count_components

def main():
    with open("input.txt", 'rb') as file:
        data = list(map(int, file.read().split()))
        v_count = data[0]
        e_count = data[1]

        graph = [[] for _ in range(v_count)]

        for i in range(2, e_count * 2 + 2, 2):
            a = data[i] - 1
            b = data[i + 1] - 1
            graph[a].append(b)
            graph[b].append(a)

    with open("output.txt", 'w') as file:
        file.write(str(dfs_iterative(graph)))

if __name__ == "__main__":
    main()

