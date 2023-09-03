def majorityElement(nums):
    hm = {}
    max_count, res = 0, 0

    for i in range(len(nums)):
        hm[nums[i]] = hm.get(nums[i], 0) + 1
        max_count = max(max_count, hm[nums[i]])
        if hm[nums[i]] == max_count:
            res = nums[i]

    return res


print(majorityElement([2, 2, 1, 1, 2, 2]))

# time complexity: o(n)
# time complexity: o(n)
