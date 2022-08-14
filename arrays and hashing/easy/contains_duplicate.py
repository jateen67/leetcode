def containsDuplicate(nums):
    elements = set()

    for i in range(len(nums)):
        if nums[i] in elements:
            return True
        elements.add(nums[i])
    return False


print(containsDuplicate([1, 2, 3, 4, 5]))
