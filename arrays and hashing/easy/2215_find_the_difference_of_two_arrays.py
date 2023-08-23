def findDifference(nums1, nums2):
    s1, s2 = set(nums1), set(nums2)
    r1, r2 = set(), set()

    for num in s1:
        if num not in s2:
            r1.add(num)

    for num in s2:
        if num not in s1:
            r2.add(num)

    return [list(r1), list(r2)]


print(findDifference([1, 2, 3], [2, 4, 6]))

# time complexity: o(m + n)
# space complexity: o(m + n)
