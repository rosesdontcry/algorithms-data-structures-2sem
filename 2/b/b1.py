with open("../c/input.txt", 'r') as file:
    c, n = map(int, file.readline().split())
    array = [list(map(int, file.readline().split())) for _ in range(n)]

    print(array)