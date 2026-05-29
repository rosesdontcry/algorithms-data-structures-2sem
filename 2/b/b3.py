def worst_case(heap_size):
    heap = [0] * heap_size

    
    heap[0] = 1

    for number in range(2, heap_size + 1):

        out_old_heap = number - 2

        index = out_old_heap
        while index > 0:
            parent_index = (index - 1) // 2
            heap[index] = heap[parent_index]
            index = parent_index

        heap[0] = number
        heap[number - 1] = 1

    return heap


with open("heapsort.in", "r") as input_file:
    n = int(input_file.readline())

out = worst_case(n)

with open("heapsort.out", "w") as output_file:
    output_file.write(" ".join(map(str, out)))