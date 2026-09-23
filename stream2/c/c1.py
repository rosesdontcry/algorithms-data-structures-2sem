def from_edges_to_lists(data):
    v_count = data[0]
    e_count = data[1]
    idx = 2

    lists = [[] for _ in range(v_count)]

    for _ in range(e_count):
        a = data[idx] - 1
        b = data[idx + 1]
        lists[a].append(b)
        idx += 2

    print_lists = [str(v_count)]
    for i in lists:
        print_lists.append((str(len(i)) + " "  + " ".join(map(str, i))).strip())

    return '\n'.join(print_lists)


def from_mat_to_lists(data):
    idx = 0
    v_count = data[0]

    lists = [[] for _ in range(v_count)]

    for i in range(v_count):
        for j in range(v_count):
            idx += 1
            if data[idx]:
                a = i
                b = j + 1
                lists[a].append(b)


    print_lists = [str(v_count)]
    for i in lists:
        print_lists.append((str(len(i)) + " "  + " ".join(map(str, i))).strip())

    return '\n'.join(print_lists)


def from_mat_to_edges(data):
    idx = 0
    v_count = data[0]
    e_count = 0

    edges = []

    for i in range(v_count):
        for j in range(v_count):
            idx += 1
            if data[idx]:
                a = i + 1
                b = j + 1
                edges.append((a, b))
                e_count += 1


    print_edges = [f"{str(v_count)} {str(e_count)}"]
    for i in edges:
        print_edges.append(" ".join(map(str, i)))

    return "\n".join(print_edges)


def from_lists_to_edges(data):
    v_count = data[0]
    e_count = 0
    idx = 1

    edges = []

    for i in range(v_count):
        lol = data[idx]
        e_count += lol
        idx += 1
        for j in range(lol):
            a = i + 1
            b = data[idx]
            edges.append((a, b))
            idx += 1

    print_edges = [str(v_count), str(e_count)]
    for i in edges:
        print_edges.append(" ".join(map(str, i)))

    return "\n".join(print_edges)


def from_edges_to_mat(data):
    v_count = data[0]
    e_count = data[1]
    idx = 2

    matrix = [[0] * v_count for _ in range(v_count)]

    for _ in range(e_count):
        a = data[idx] - 1
        b = data[idx + 1] - 1
        matrix[a][b] = 1
        idx += 2

    print_matrix = [str(v_count)]
    for i in matrix:
        print_matrix.append(" ".join(map(str, i)))

    return "\n".join(print_matrix)


def from_lists_to_mat(data):
    v_count = data[0]
    idx = 1

    matrix = [[0] * v_count for _ in range(v_count)]

    for i in range(v_count):
        e_count = data[idx]
        idx += 1
        for j in range(e_count):
            a = i
            b = data[idx] - 1
            matrix[a][b] = 1
            idx += 1

    print_matrix = [str(v_count)]
    for i in matrix:
        print_matrix.append(" ".join(map(str, i)))

    return "\n".join(print_matrix)


def print_to_file(data):
    with open("output.txt", 'w') as file:
        file.write(data)


def main():
    with open("input.txt", 'r') as file:
        enter = file.readline().strip()
        data = list(map(int, file.read().split()))
    
    
    match enter:
        case "edges mat":
            print_to_file(from_edges_to_mat(data))
        case "edges lists":
            print_to_file(from_edges_to_lists(data))
        case "mat edges":
            print_to_file(from_mat_to_edges(data))
        case "mat lists":
            print_to_file(from_mat_to_lists(data))
        case "lists edges":
            print_to_file(from_lists_to_edges(data))
        case "lists mat":
            print_to_file(from_lists_to_mat(data))

    
if __name__ == "__main__":
    main()

