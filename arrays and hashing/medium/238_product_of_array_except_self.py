def prod(nums):
    res = [1] * len(nums)

    pre, post = 1, 1

    for i in range(len(nums)):
        res[i] = pre
        pre *= nums[i]

    for i in range(len(nums) - 1, -1, -1):
        res[i] *= post
        post *= nums[i]

    return res


print(prod([1, 2, 3, 4, 5]))

# time complexity: o(n)
# space complexity: o(1)
