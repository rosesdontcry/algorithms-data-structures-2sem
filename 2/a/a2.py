def povar(a1, arr1):
    maxim = 0
    nemaxim = 0

    for i in range(len(arr1)):
        if arr1[i] > maxim:
            nemaxim = maxim
            maxim = arr1[i]
        elif arr[i] != maxim:
            if arr1[i] > nemaxim:
                nemaxim = arr1[i]

    return nemaxim

a = int(input())
arr = [int(i) for i in input().split()]


print(povar(a, arr))

