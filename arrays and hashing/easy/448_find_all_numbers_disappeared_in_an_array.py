def findDisappearedNumbers(nums):
    res = []

    for i in range(len(nums)):
        idx = abs(nums[i]) - 1

        if nums[idx] > 0:
            nums[idx] *= -1

    for i in range(len(nums)):
        if nums[i] > 0:
            res.append(i + 1)

    return res


print(findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))

# time complexity: o(n)
# time complexity: o(1)
