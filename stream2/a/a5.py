def func(temp_n, temp_a, temp_b):
    return temp_n*(temp_a - temp_b*temp_n)


def ternary_search(temp_n, temp_a, temp_b):
    left_border = 1
    right_border = temp_n
    eps = 1e-9
    rational_function = lambda x: func(x, temp_a, temp_b)

    while abs(right_border - left_border) > 2:
        left_point = (2 * left_border + right_border) // 3
        right_point = (left_border + 2 * right_border) // 3

        if rational_function(left_point) < rational_function(right_point):
            left_border = left_point
        else:
            right_border = right_point

    print(max(rational_function(i) for i in range(int(left_border), int(right_border)+1)))
    return -1


n, a, b = map(int, input().split())

ternary_search(n, a, b)
