def sift_down_max(arr, t, size):
    """
    Просеивает элемент arr[t] вниз по куче размером size.
    arr   — массив, представляющий кучу
    t     — индекс элемента, который нужно просеять
    size  — сколько элементов считать кучей (остаток массива уже отсортирован)
    """
    while True:
        largest = t           # предполагаем, что текущий узел — наибольший
        left    = 2 * t + 1   # индекс левого ребёнка
        right   = 2 * t + 2   # индекс правого ребёнка

        # Если левый ребёнок существует и больше текущего «наибольшего»
        if left < size and arr[left] > arr[largest]:
            largest = left

        # Если правый ребёнок существует и больше текущего «наибольшего»
        if right < size and arr[right] > arr[largest]:
            largest = right

        # Если наибольший — уже сам узел, свойство кучи выполнено, стоп
        if largest == t:
            break

        # Меняем текущий узел с наибольшим ребёнком
        arr[t], arr[largest] = arr[largest], arr[t]

        # Продолжаем просеивание с новой позиции
        t = largest


def sift_down_min(arr, t, size):
    """
    Просеивает элемент arr[t] вниз по куче размером size.
    arr   — массив, представляющий кучу
    t     — индекс элемента, который нужно просеять
    size  — сколько элементов считать кучей (остаток массива уже отсортирован)
    """
    while True:
        largest = t           # предполагаем, что текущий узел — наибольший
        left    = 2 * t + 1   # индекс левого ребёнка
        right   = 2 * t + 2   # индекс правого ребёнка

        # Если левый ребёнок существует и больше текущего «наибольшего»
        if left < size and arr[left] < arr[largest]:
            largest = left

        # Если правый ребёнок существует и больше текущего «наибольшего»
        if right < size and arr[right] < arr[largest]:
            largest = right

        # Если наибольший — уже сам узел, свойство кучи выполнено, стоп
        if largest == t:
            break

        # Меняем текущий узел с наибольшим ребёнком
        arr[t], arr[largest] = arr[largest], arr[t]

        # Продолжаем просеивание с новой позиции
        t = largest


def sift_up_max(arr, t):
    """
    Просеивает элемент arr[t] вверх по куче.
    arr — массив, представляющий кучу
    t   — индекс только что добавленного элемента
    """
    while t > 0:
        parent = (t - 1) // 2   # индекс родителя

        # Если текущий элемент больше родителя — меняемся и идём выше
        if arr[t] > arr[parent]:
            arr[t], arr[parent] = arr[parent], arr[t]
            t = parent
        else:
            break               # свойство кучи выполнено, стоп

def sift_up_min(arr, t):
    """
    Просеивает элемент arr[t] вверх по куче.
    arr — массив, представляющий кучу
    t   — индекс только что добавленного элемента
    """
    while t > 0:
        parent = (t - 1) // 2   # индекс родителя

        # Если текущий элемент больше родителя — меняемся и идём выше
        if arr[t] < arr[parent]:
            arr[t], arr[parent] = arr[parent], arr[t]
            t = parent
        else:
            break


with open("../c/input.txt", "r") as file:
    _ = file.readline()
    enter = list(map(int, file.readline().split()))

left_heap_min = []
right_heap_max = []
out = []

for i in enter:
    if not right_heap_max or right_heap_max[0] >= i:
        right_heap_max.append(i)
        sift_up_max(right_heap_max, len(right_heap_max) - 1)
    else:
        left_heap_min.append(i)
        sift_up_min(left_heap_min, len(left_heap_min) - 1)


    if len(right_heap_max) - len(left_heap_min) > 1:
        right_heap_max[0], right_heap_max[-1] = right_heap_max[-1], right_heap_max[0]
        left_heap_min.append(right_heap_max.pop())
        sift_down_max(right_heap_max, 0, len(right_heap_max))
        sift_up_min(left_heap_min, len(left_heap_min) - 1)
    elif len(left_heap_min) - len(right_heap_max) > 0:
        left_heap_min[0], left_heap_min[-1] = left_heap_min[-1], left_heap_min[0]
        right_heap_max.append(left_heap_min.pop())
        sift_down_min(left_heap_min, 0, len(left_heap_min))
        sift_up_max(right_heap_max, len(right_heap_max) - 1)

    out.append(right_heap_max[0])

with open("../c/output.txt", "w") as file:
    file.write(' '.join(map(str, out)))