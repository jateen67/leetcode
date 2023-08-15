def getConcatenation(nums):
    res = []

    for i in range(2 * len(nums)):
        res.append(nums[i % len(nums)])

    return res


print(getConcatenation([1, 2, 1]))

# time complexity: o(2n)
# space complexity: o(2n)
