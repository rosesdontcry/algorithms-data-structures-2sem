def condition(a1 , a2):
    if a1[1] != a2[1]:
        return a1[1] < a2[1]
    return a1[0] < a2[0]


def sift_down(arr, t, size):
    while True:
        smallest = t           # предполагаем, что текущий узел — наибольший
        left    = 2 * t + 1   # индекс левого ребёнка
        right   = 2 * t + 2   # индекс правого ребёнка

        # Если левый ребёнок существует и больше текущего «наибольшего»
        if left < size and condition(arr[left], arr[smallest]):
            smallest = left
        # Если правый ребёнок существует и больше текущего «наибольшего»
        if right < size and condition(arr[right], arr[smallest]):
            smallest = right

        # Если наибольший — уже сам узел, свойство кучи выполнено, стоп
        if smallest == t:
            break

        # Меняем текущий узел с наибольшим ребёнком
        arr[t], arr[smallest] = arr[smallest], arr[t]

        # Продолжаем просеивание с новой позиции
        t = smallest


def sift_up(arr, t):
    while t > 0:
        parent = (t - 1) // 2   # индекс родителя

        # Если текущий элемент больше родителя — меняемся и идём выше
        if condition(arr[t], arr[parent]):
            arr[t], arr[parent] = arr[parent], arr[t]
            t = parent
        else:
            break               # свойство кучи выполнено, стоп


def pop0_from_heap(t_heap):
    old = t_heap[0]
    new = t_heap.pop()
    if heap:
        heap[0] = new
        sift_down(t_heap, 0, len(t_heap))
    return old


def add_to_heap(t_heap, t_num):
    t_heap.append(t_num)
    sift_up(t_heap, len(t_heap) - 1)


with open("../c/input.txt", 'r') as file:
    num_of_num, num_of_oper = map(int, file.readline().split())
    numbers = list(map(int, file.readline().split()))

heap = []
for j in range(num_of_num):
    add_to_heap(heap, [j, numbers[j]])

index = num_of_num

for _ in range(num_of_oper):
    x1 = pop0_from_heap(heap)
    x2 = pop0_from_heap(heap)

    add_to_heap(heap, [index, x1[1] + x2[1]])
    index += 1


result = [None] * index
for i, num in heap:
    result[i] = num


with open("../c/output.txt", 'w') as file:
    file.write(' '.join([str(i) for i in result if i is not None]))


