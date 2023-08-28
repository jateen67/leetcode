def moveZeroes(nums):
    l = 0

    for r in range(len(nums)):
        if nums[r] != 0:
            tmp = nums[l]
            nums[l] = nums[r]
            nums[r] = tmp
            l += 1

    return nums


print(moveZeroes([1, 0, 3, 2]))

# time complexity: o(n)
# time complexity: o(1)
