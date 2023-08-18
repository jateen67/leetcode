def searchInsert(nums, target):
    l, r = 0, len(nums) - 1
    mid = 0

    while l <= r:
        mid = (l + r) // 2

        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            r = mid - 1
        else:
            l = mid + 1

    return mid + 1 if target > nums[mid] else mid


print(searchInsert([1, 3, 5, 6], 2))

# time complexity: o(logn)
# space complexity: o(1)
