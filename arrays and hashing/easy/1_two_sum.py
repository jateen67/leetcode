def twoSum(nums, target):
    h = {}

    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in h:
            return [h[diff], i]
        h[nums[i]] = i


print(twoSum([1, 2, 3, 4, 5, 6], 11))

# time complexity: o(n)
# space complexity: o(n)
