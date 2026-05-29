def main():
    array = [0] * 2001

    with open('../c/input.txt', 'r') as file:
        _ = file.readline()

        num = ''
        while True:
            piece = file.read(16384)
            if not piece:
                break

            for char in piece:
                if char != '\n' and char != ' ':
                    num += char
                else:
                    array[int(num) + 1000] += 1
                    num = ''
        if num:
            array[int(num) + 1000] += 1

    with open('../c/output.txt', 'w') as file:
        for i in range(len(array)):
            if array[i] > 0:
                file.write(f"{i - 1000} {array[i]}\n")


if __name__ == '__main__':
    main()