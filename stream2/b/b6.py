def quick_sort(arr):
    if len(arr) <= 1:
        return arr                      # базовый случай: 0 или 1 элемент уже отсортирован

    pivot = arr[len(arr) // 2]          # выбираем средний элемент как опорный
    left  = [x for x in arr if x[0] < pivot[0] or (x[0] == pivot[0] and x[1] > pivot[1])]   # всё, что меньше pivot
    mid   = [x for x in arr if x[0] == pivot[0] and x[1] == pivot[1]]  # сам pivot (может встречаться несколько раз)
    right = [x for x in arr if x[0] > pivot[0] or (x[0] == pivot[0] and x[1]< pivot[1])]   # всё, что больше pivot

    return quick_sort(left) + mid + quick_sort(right)


n = int(input())
couples = [list(map(int, input().split())) for _ in range(n)]

couples = quick_sort(couples)

_ = [print(f"{x[0]} {x[1]}") for x in couples]
