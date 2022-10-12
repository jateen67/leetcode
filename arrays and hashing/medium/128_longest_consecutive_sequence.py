def longest(nums):
    if not nums:
        return 0

    hs = set(nums)
    res = 0

    for i in range(len(nums)):
        if nums[i] - 1 not in hs:
            seq_len = 0
            while nums[i] + seq_len in hs:
                seq_len += 1
            res = max(res, seq_len)

    return res


arr = [100, 4, 200, 1, 3, 2]
print(longest(arr))

# time complexity: o(n)
# space complexity: o(n)
