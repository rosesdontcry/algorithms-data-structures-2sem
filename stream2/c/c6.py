def bellman_ford(v_count, edges, start):
    distances = [float('inf')] * v_count
    distances[start] = 0
    
    for i in range(v_count - 1):
        updated = False
        
        for a, b , weight in edges:
            if distances[a] == float('inf'):
                continue
                
            new_distance = distances[a] + weight
            if new_distance < distances[b]:
                distances[b] = new_distance
                updated = True
        
        if not updated:
            break
            
    return distances


def main():
    with open("input.txt", 'rb') as file:
        v_count, e_count, start = map(int, file.readline().split())
        start -= 1

        graph = []
        for _ in range(e_count):
            vertex, neighbour, weight = map(int, file.readline().split())
            vertex -= 1
            neighbour -= 1
            graph.append((vertex, neighbour, weight))

    distances = bellman_ford(v_count, graph, start)

    with open("output.txt", 'w') as file:
        file.write(' '.join([' ' if x == float('inf') else str(x) for x in distances]))


if __name__ == "__main__":
    main()
