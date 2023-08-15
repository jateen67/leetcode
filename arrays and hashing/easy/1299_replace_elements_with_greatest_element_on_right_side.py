def replaceElements(arr):
    greatest = -1

    for i in range(len(arr) - 1, -1, -1):
        tmp = arr[i]
        arr[i] = greatest
        greatest = max(greatest, tmp)

    return arr


print(replaceElements([17, 18, 5, 4, 6, 1]))

# time complexity: o(n)
# space complexity: o(1)
