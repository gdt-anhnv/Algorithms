def ParentIndex(i) :
    return i + i & (-i)

def Update(arr, i, val) :
    while i < len(arr):
        arr[i] += val
        i = ParentIndex(i)

    return

def FenwickTree() :
    arr = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
    fenwick = [0] * (len(arr) + 1)
    for i in range(0, len(arr), 1) :
        Update(fenwick, i + 1, arr[i])

    print str(fenwick)[1:-1]

    return

FenwickTree()