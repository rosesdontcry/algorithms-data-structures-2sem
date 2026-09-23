def worst_heap(size):
    heap = []

    if size == 1:
        return [1]

    for num in range(2, n+1):
        heap.append(num)
        sift_up(heap, len(heap) - 1)

    heap.append(1)
    return heap


def sift_up(arr, i):
    """
    Просеивает элемент arr[i] вверх по куче.
    arr — массив, представляющий кучу
    i   — индекс только что добавленного элемента
    """
    while i > 0:
        parent = (i - 1) // 2   # индекс родителя

        # Если текущий элемент больше родителя — меняемся и идём выше
        if arr[i] > arr[parent]:
            arr[i], arr[parent] = arr[parent], arr[i]
            i = parent
        else:
            break               # свойство кучи выполнено, стоп


with open("../2/b/heapsort.in", "r") as input_file:
    n = int(input_file.readline())

    out = worst_heap(n)

with open("../2/b/heapsort.out", "w") as output_file:
    output_file.write(" ".join(map(str, out)))

# n = [2]
# n.append(3)
# sift_up(n, len(n)-1)
# n.append(4)
# sift_up(n, len(n)-1)
# n.append(5)
# sift_up(n, len(n)-1)
# n.append(6)
# sift_up(n, len(n)-1)
# print(n)
#

