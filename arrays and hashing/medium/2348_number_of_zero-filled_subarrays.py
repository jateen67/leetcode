def zeroFilledSubarray(nums):
    count, res = 0, 0

    for num in nums:
        if num == 0:
            count += 1
        else:
            count = 0
        res += count

    return res


print(zeroFilledSubarray([0, 0, 2, 0, 0]))

# time complexity: o(n)
# space complexity: o(1)
