def minimumDifference(nums, k):
    nums.sort()
    l = 0
    res = float("inf")

    for r in range(k - 1, len(nums)):
        diff = nums[r] - nums[l]
        res = min(res, diff)
        l += 1

    return res


print(minimumDifference([9, 4, 1, 7], 2))

# time complexity: o(nlog(n))
# space complexity: o(1)
