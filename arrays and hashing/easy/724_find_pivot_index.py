def pivotIndex(nums):
    left_sum, right_sum = 0, sum(nums)

    for i in range(len(nums)):
        right_sum -= nums[i]

        if left_sum == right_sum:
            return i

        left_sum += nums[i]


print(pivotIndex(1, 7, 3, 6, 5, 6))

# time complexity: o(n)
# time complexity: o(1)
