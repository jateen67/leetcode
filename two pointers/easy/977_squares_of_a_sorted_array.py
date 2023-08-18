def sortedSquares(nums):
    l, r = 0, len(nums) - 1
    res = [0] * len(nums)
    p = len(nums) - 1

    while l <= r:
        if nums[l] ** 2 > nums[r] ** 2:
            res[p] = nums[l] ** 2
            l += 1
        else:
            res[p] = nums[r] ** 2
            r -= 1
        p -= 1

    return res


print(sortedSquares([-4, -1, 0, 3, 10]))

# time complexity: o(n)
# space complexity: o(n)
