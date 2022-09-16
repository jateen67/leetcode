def single(nums):
    res = 0
    for i in range(len(nums)):
        res = res ^ nums[i]
    return res


print(single([2, 2, 1]))

# time complexity: o(n)
# space complexity: o(1)
