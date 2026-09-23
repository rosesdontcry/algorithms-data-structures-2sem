def ifelse(n1, k1, arr1):
    #if k not in arr:
    #    return -1
    for i in range(n1):
        if arr1[i] == k1:
            return i+1
    else:
        return -1



n, k = [int(i) for i in input().split()]
arr = [int(i) for i in input().split()]

print(ifelse(n, k, arr))
