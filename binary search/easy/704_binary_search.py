def search(nums, target):
    l = 0
    r = len(nums) - 1

    while l <= r:
        mid = (l + r) // 2
        if target == nums[mid]:
            return mid
        if target < nums[mid]:
            r = mid - 1
        else:
            l = mid + 1
    return -1


print(search([-1, 0, 3, 5, 9, 12], 9))

# time complexity: o(log(n))
# space complexity: o(1)
