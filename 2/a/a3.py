def stepka(t1, n1, arr1):
    if t1 > arr1[n1-1]:
        return -1
    if t1 <= arr1[0]:
        return arr1[0]

    l, r = 0, n1 -1

    while r - l > 1:
        m = (l + r) // 2
        if arr1[m] == t1:
            return arr[m]
        elif arr1[m] > t1:
            r = m
        else:
            l = m
    return arr1[r]

n, t = [int(i) for i in input().split()]
arr = [int(i) for i in input().split()]

print(stepka(t, n , arr))
