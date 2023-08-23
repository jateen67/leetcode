def numOfSubArrays(arr, k, threshold):
    l = 0
    total = sum(arr[: k - 1])
    res = 0

    for r in range(k - 1, len(arr)):
        total += arr[r]

        if total / k >= threshold:
            res += 1

        total -= arr[l]
        l += 1

    return res


print(numOfSubArrays([11, 13, 17, 23, 29, 31, 7, 5, 2, 3], 3, 5))

# time complexity: o(n)
# time complexity: o(1)
