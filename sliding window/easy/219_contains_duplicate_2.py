def containsNearbyDuplicate(nums, k):
    # hm = {}

    # for i in range(len(nums)):
    #     if nums[i] in hm and abs(i - hm[nums[i]] <= k):
    #         return True

    #     hm[nums[i]] = i

    # return False
    s = set()
    l = 0

    for r in range(len(nums)):
        if r - l > k:
            s.remove(nums[l])
            l += 1

        if nums[r] in s:
            return True

        s.add(nums[r])

    return False


print(containsNearbyDuplicate([1, 2, 3, 1], 3))

# time complexity: o(n)
# space complexity: o(k)
