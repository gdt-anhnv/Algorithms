def Heapify(arr, n, i) :
    largestIndex = i
    leftIndex = i * 2 + 1
    rightIndex = i * 2 + 2

    if leftIndex < n and arr[largestIndex] < arr[leftIndex] :
        largestIndex = leftIndex

    if rightIndex < n and arr[largestIndex] < arr[rightIndex] :
        largestIndex = rightIndex

    if largestIndex != i :
        arr[i],arr[largestIndex] = arr[largestIndex],arr[i]
        Heapify(arr, n, largestIndex)
    return

def HeapSort() :
    arr = [19, 7, 21, 1, 17, 34, 10, 9, 12, 66, 3]
    for i in range(len(arr)//2 - 1, -1, -1) :
        print i
        Heapify(arr, len(arr), i)

    print str(arr)[1:-1]

    for i in range(len(arr) - 1, 0, -1) :
        arr[i], arr[0] = arr[0], arr[i]
        Heapify(arr, i, 0)

    print str(arr)[1:-1]
    return

HeapSort()