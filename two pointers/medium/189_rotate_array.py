def rotate(nums, k):
    if len(nums) == 1:
        return nums

    k %= len(nums)

    l, r = 0, len(nums) - 1

    while l < r:
        tmp = nums[l]
        nums[l] = nums[r]
        nums[r] = tmp
        l += 1
        r -= 1

    l, r = 0, k - 1

    while l < r:
        tmp = nums[l]
        nums[l] = nums[r]
        nums[r] = tmp
        l += 1
        r -= 1

    l, r = k, len(nums) - 1

    while l < r:
        tmp = nums[l]
        nums[l] = nums[r]
        nums[r] = tmp
        l += 1
        r -= 1

    return nums


print(rotate([1, 2, 3, 4, 5, 6, 7], 3))

# time complexity: o(n)
# time complexity: o(1)
