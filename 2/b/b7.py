def bucket_sort(tarr):
    for char in range(3):
        buckets = [[] for _ in range(65, 123)]

        for string in tarr:
            char_value = ord(string[abs(char - 2)]) - 65
            buckets[char_value].append(string)

        tarr = []
        for bucket in buckets:
            tarr.extend(bucket)

    return tarr


with open("../c/input.txt", 'r') as file:
    n = int(file.readline())
    array = [file.readline().strip() for _ in range(n)]

    array = bucket_sort(array)

with open("../c/output.txt", 'w') as file:
    for i in array:
        file.write(f"{i}\n")

