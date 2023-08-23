def arraySign(nums):
    res = 0

    for num in nums:
        if num == 0:
            return 0
        if num < 0:
            res += 1

    return 1 if res % 2 == 0 else -1


print(arraySign([1, 2, 1]))

# time complexity: o(n)
# space complexity: o(1)
